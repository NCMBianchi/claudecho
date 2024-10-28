######################################
## CHATGPT clone, © Niccolò Bianchi ##
######################################

## This CLI is based on a youtube video guide, and implements a
## simple client-server with OpenAI's API for chatgpt. This version
## only works with API version <1.0.0 and it's NOT mean for
## commercial use.


# handles the key securely
import os

# handles the command line, things related to the command line and pass commands
import typer

# handles everything related to ChatGPT functionality
import openai

# allows for the openAI API key to be accessible
from dotenv import load_dotenv

# allows to run a parameter as optional
from typing import Optional

# load API key
load_dotenv()
api_key = os.getenv("OPENAI_KEY")

# initialize OpenAI client
client = openai.OpenAI(api_key=api_key)
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
        "gpt-4o-mini", "--model", "-m", help="Chooses a model."
    ),
):
    """
    Interactive CLI tool to chat with ChatGPT.

    Models available:\n
      - gpt-4o          Most advanced model. Costs $2.50 per 1M input tokens, $10.00 per 1M output tokens.\n
      - gpt-4o-mini     Faster and optimised. Costs $0.15 per 1M input tokens, $0.60 per 1M output tokens.\n
      - gpt-o1-preview  For complex tasks. Costs $15.00 per 1M input tokens, $60.00 per 1M output tokens.\n
      - gpt-o1-mini     Fast reasoning model. Costs $3.00 per 1M input tokens, $12.00 per 1M output tokens.
    """
    typer.echo(
        f"Starting interactive chat with ChatGPT version '{model}'. Type '/bye' to end the session.\n"
    )
    if text:
        print(f'You: {text}')

    messages = []

    i = 1
    while True:
        if i == 1 and text:
            prompt = text
        else:
            prompt = input("You: ")
        i += 1

        if prompt.lower() == "/bye":
            typer.echo("ChatGPT: Goodbye!")
            break

        messages.append({"role": "user", "content": prompt})

        # use the client to create chat completions
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )

        # access response content (it avoids empty lines, but paragraphs are no longer possible)
        cleaned_response = response.choices[0].message.content.replace("\n", " ")
        typer.echo(f'ChatGPT: {cleaned_response}')
        messages.append({"role": "assistant", "content": cleaned_response})

if __name__ == "__main__":
    app()


