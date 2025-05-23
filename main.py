##################################
## CLAUDECHO, © Niccolò Bianchi ##
##################################

## This CLI for a simple client-server with Anthropic's API for 
## Claude is the fork of another similar tool I made for OpenAI's
## API for chatgpt.


# handles the key securely
import os

# handles the command line, things related to the command line and pass commands
import typer

# handles everything related to Claude's API functionality
from anthropic import Anthropic, BadRequestError

# allows for the openAI API key to be accessible
from dotenv import load_dotenv

# allows to run a parameter as optional
from typing import Optional

# load API key
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# initialize OpenAI client
client = Anthropic(api_key=api_key)
app = typer.Typer(add_completion=False)

# Set interactive_chat as the default command
@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Anthropic Claude interactive CLI."""
    if ctx.invoked_subcommand is None:
        interactive_chat()

# actual tool functionality
def create_message(model, messages, max_tokens, temperature, web_search=False, thinking_mode=False):
    """Create a message with the appropriate parameters based on enabled features."""
    common_params = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    if web_search:
        # For web search, we need to add tools parameter
        # Note: This is compatible with Claude 3.5+ and 3.7+ models
        common_params["tools"] = [{"type": "web_search"}]
    elif thinking_mode:
        # For thinking mode, we add a system prompt
        common_params["system"] = "When answering, first think step-by-step through the problem before providing your final answer."
    
    return client.messages.create(**common_params)

def get_response_text(response):
    """Extract text content from response."""
    if not response or not hasattr(response, 'content') or not response.content:
        return "No response content available."
    
    # Get the first text content from the response
    for content_block in response.content:
        if hasattr(content_block, 'content') and content_block.content:
            return content_block.content
        if hasattr(content_block, 'text') and content_block.text:
            return content_block.text
    
    # Fallback if no text content found
    return str(response)

def has_tool_usage(response):
    """Check if response used a tool."""
    if not response or not hasattr(response, 'content'):
        return False
    
    for content_block in response.content:
        content_type = getattr(content_block, 'type', None)
        if content_type == "tool_use":
            return True
    return False

@app.command()
def list_models():
    """
    Display all available Claude models and their descriptions.
    """
    typer.echo("Available Claude Models:\n")
    typer.echo("  - claude-opus-4-20250514       Latest Claude 4 Opus model, powerful for complex tasks.")
    typer.echo("  - claude-sonnet-4-20250514     Faster, more affordable Claude 4 Sonnet model.")
    typer.echo("  - claude-3-opus-20240229       Most capable Claude 3 model for complex tasks.")
    typer.echo("  - claude-3-sonnet-20240229     Balanced Claude 3 model for most use cases.")
    typer.echo("  - claude-3-haiku-20240307      Fastest Claude 3 model for shorter tasks.")
    typer.echo("\nUse with: main.sh -m \"model-name\" or main.sh --model \"model-name\"")

@app.command()
def interactive_chat(
    text: Optional[str] = typer.Option(None, "--text", "-t", help="Starts with an initial message text."),
    temperature: float = typer.Option(0.7, "--temp", "-T", help="Sets the temperature (randomness) from 0 to 1."),
    max_tokens: int = typer.Option(
        150, "--maxtokens", "-M", help="Sets the maximum response length."
    ),
    model: str = typer.Option(
        "claude-sonnet-4-20250514", "--model", "-m", help="Chooses a model."
    ),
    web_search: bool = typer.Option(
        False, "--websearch", "-w", help="Enables web search capability."
    ),
    thinking_mode: bool = typer.Option(
        False, "--thinking", "-k", help="Enables thinking mode to see Claude's reasoning process."
    ),
):
    """
    Interactive CLI tool to chat with Anthropic's Claude.

    Models available:\n
      - claude-opus-4-20250514       Latest Claude 4 Opus model, powerful for complex tasks.\n
      - claude-sonnet-4-20250514     Faster, more affordable Claude 4 Sonnet model.\n
      - claude-3-opus-20240229       Most capable Claude 3 model for complex tasks.\n
      - claude-3-sonnet-20240229     Balanced Claude 3 model for most use cases.\n
      - claude-3-haiku-20240307      Fastest Claude 3 model for shorter tasks.
      
    Options:\n
      --websearch / -w             Enable web search capability (requires Claude 3.5+ or 3.7+ model).\n
      --thinking / -k              Enable thinking mode to see Claude's reasoning process.
    """
    typer.echo(
        f"Starting interactive chat with Claude version '{model}'. Type '/bye' to end the session.\n"
    )
    if text:
        print(f'You: {text}')

    messages = []
    try:
        while True:
            if text and not messages:  # only uses 'text' for the first message
                prompt = text
            else:
                prompt = input("You: ")
                
            if prompt.lower() == "/bye":
                typer.echo("Claude: Goodbye!")
                break

            messages.append({"role": "user", "content": prompt})
            
            try:
                # Try to create a message with the requested features
                try:
                    response = create_message(
                        model=model,
                        messages=messages,
                        max_tokens=max_tokens,
                        temperature=temperature,
                        web_search=web_search,
                        thinking_mode=thinking_mode
                    )
                except Exception as e:
                    # If web search fails, try without it
                    if web_search:
                        typer.echo(f"Web search error: {str(e)}. Make sure you're using a compatible model (Claude 3.5+ or 3.7+).")
                        web_search = False
                        response = create_message(
                            model=model,
                            messages=messages,
                            max_tokens=max_tokens,
                            temperature=temperature,
                            thinking_mode=thinking_mode
                        )
                    else:
                        raise
                
                # Extract and process the response text
                try:
                    response_text = get_response_text(response)
                    cleaned_response = response_text.replace("\n", " ")
                    
                    # Display response with appropriate prefix
                    tool_used = has_tool_usage(response)
                    
                    if web_search and tool_used:
                        typer.echo(f'Claude (using web search): {cleaned_response}')
                    elif thinking_mode:
                        typer.echo(f'Claude (thinking mode): {cleaned_response}')
                    else:
                        typer.echo(f'Claude: {cleaned_response}')
                        
                    # Add response to conversation history
                    messages.append({"role": "assistant", "content": cleaned_response})
                    
                except Exception as e:
                    typer.echo(f'Error processing response: {str(e)}')
                    fallback_response = "I encountered an error processing my response."
                    typer.echo(f'Claude: {fallback_response}')
                    messages.append({"role": "assistant", "content": fallback_response})
                
            except BadRequestError as e:
                if "credit balance is too low" in str(e):
                    typer.echo("Error: Insufficient credits in your Anthropic account. Please add more credits at https://console.anthropic.com/")
                    break
                else:
                    # re-raised if it's a different type of BadRequestError
                    raise
                    
    except KeyboardInterrupt:
        typer.echo("\nChat session terminated by user.")
    except Exception as e:
        typer.echo(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    app()


