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

# actual tool functionality
@app.command()
def interactive_chat(
    text: Optional[str] = typer.Option(None, "--text", "-t", help="Starts with an initial message text."),
    temperature: float = typer.Option(0.7, "--temp", "-T", help="Sets the temperature (randomness) from 0 to 1."),
    max_tokens: int = typer.Option(
        150, "--maxtokens", "-M", help="Sets the maximum response length."
    ),
    model: str = typer.Option(
        "claude-3-sonnet-20240229", "--model", "-m", help="Chooses a model."
    ),
):
    """
    Interactive CLI tool to chat with Anthropic's Claude.

    Models available:\n
      - claude-3-opus-20240229      Most capable model for complex tasks.\n
      - claude-3-sonnet-20240229    Balanced model for most use cases.\n
      - claude-3-haiku-20240307     Fastest model for shorter tasks.
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
                # uses the client to create chat completions
                response = client.messages.create(
                    model=model,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature
                )
                
                # access response content (it avoids empty lines, but paragraphs are no longer possible)
                cleaned_response = response.content[0].text.replace("\n", " ")
                typer.echo(f'Claude: {cleaned_response}')
                messages.append({"role": "assistant", "content": cleaned_response})
                
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


