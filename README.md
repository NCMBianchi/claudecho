# 'CLAUDEcho' interactive CLI

![image-1](https://github.com/user-attachments/assets/cb0e98e4-4734-4721-bfab-9db1c4a0e6fb)

This <b>interactive CLI for Claude</b> is based on another proof-of-concept project to make queries to Claude.

More information on Anthropic's API on: [https://docs.anthropic.com/en/api/getting-started](https://docs.anthropic.com/en/api/getting-started)


## INSTRUCTIONS
### Set-up instructions (MacOS/Linux)
This tool requires <bi>pip</bi> to already be installed on the device, to then install Python package ```pyenv```.

Clone the directory with the `git clone https://github.com/NCMBianchi/claudecho.git` command in your terminal. I suggest placing it in your root directory.

Move to the directory with the `cd claudecho` command, and then activate the executable with the `chmod +x main.sh` command. Make a `.env` file storing your own 'API project key' from Anthropic's console –more info on this in a latter section.

I suggest to then add the `alias claudecho="cd ~/claudecho && ./main.sh"` line to your shell's configuration file (assuming it was installed in the root directory) so that you can exucute all following commands just using the alias in the terminal. I suggest to do this only if you are comfortable editing your shell's configuration file (<i>i.e.</i> `.zshrc` for Zsh, `.bashrc` for Bash, `.config/fish/config.fish` for Fish): if so, edit it with Vim –or any other text editor of choice- adding the alias line at the end of the document. If you are not sure which shell your terminal is using, run the `echo $SHELL` command.

### Use instructions (MacOS/Linux)

Queries can be performed with the `claudecho -t "_________"` (`main.sh -t "_______"` if the alias was not setup, as long as you are in the tools directory –which can be accesed with the `cd ~/claudecho` command, if the repository was cloned in the root directory), adding your query between quote marks.

| Short command | Full command | Description                                    | Default value   |
|---------------|--------------|------------------------------------------------|-----------------|
| -t            | --text       | Starts with an initial message text.           |                 |
| -T            | --temp       | Sets the temperature (randomness) from 0 to 1. | 0.7             |
| -M            | --maxtokens  | Sets the maximum response length.              | 150             |
| -m            | --model      | Chooses a model.                               | claude-3-sonnet |

These are all the commands that can be used in the tool, and they all required values to be inputted between quotation marks.

Moreover, the `claudecho --help` command allows to display this very table within the tool.

<img width="807" alt="Screenshot 2024-11-03 alle 11 46 12" src="https://github.com/user-attachments/assets/8a261c39-3035-4786-b051-83e8914454e4">

### API key instructions
To use this, you have to first get your own API key from [Anthropic's console](https://console.anthropic.com).

<img width="1140" alt="Screenshot 2024-11-03 alle 11 42 29-EDIT" src="https://github.com/user-attachments/assets/da23a8b0-88be-4b73-b9ac-8240f6de8dd5">

Then create a <bi>.env</bi> file with this line: `ANTHROPIC_API_KEY="____"` filling it with your own API key. Place it in the cloned directory.

### venv instructions (MacOS/Linux)
If you want to remove the virtual environment created by this tool, just use the `pyenv virtualenv-delete claudecho` command in your terminal: this will delete the virtual environment and all the packages within it. If you want to also remove Python package ```pyenv``` entirely, use the `pip uninstall pyenv` command, which requires a Y/n confirmation. First check no other functionality in your device is using them: you can check it with commands `pyenv versions` and `pyenv virtualenvs`.


##
<b> This is NOT a commercial product. The Anthropic logo mixed with the style of the 'Terminal' MacOS app icon in the image at top is used to convey the fact that the API keys used are official, according to fair use. </b>
