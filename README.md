# chatGPT clone

![Screenshot 2024-03-28 alle 09 52 03-EDIT](https://github.com/NCMBianchi/chatGPTclone/assets/111352723/2e92e2f1-7307-4707-bc89-3646018e4af1)

A proof-of-concept project on how to build an <b>interactive CLI for chatGPT</b> queries through their own API, based on a video by Warp: https://www.youtube.com/watch?v=7p7kJvckrFE

Few changes were made to the original code to allow for correct formatting, subsequent questions without the code breaking up and some minorly customised output lines. <b> Requires python package ```openai<1.0.0```.</b>

## INSTRUCTIONS
### Use instructions

Once cloned, by accessing the directory chatGPT 3.5turbo (by default), it can be queried with `python main.py -t "_____________"`, adding your query between quote marks.

The `python main.py --help` command allows to access the help window with further commands.

![Screenshot 2024-03-28 alle 10 17 28](https://github.com/NCMBianchi/chatGPTclone/assets/111352723/0ad58198-98fb-45ae-a54b-8ca3e88845c0)

One could also implement an alias for `python main.py` in their own <b>.zshrc</b> file –or the configuration file of their shell of choice. Obviously also adapt it to the python path set in the source file (<i>e.g.</i> python3).

### API key instructions
To use this, you have to first get your own API key from OpenAI.

![Screenshot 2024-03-28 alle 10 09 25-EDIT](https://github.com/NCMBianchi/chatGPTclone/assets/111352723/5c57a21a-7e4b-4e47-8374-5c3393840abf)

Then create a <bi>.env</bi> file with this line: `OPENAI_KEY="____"` filling it with your own API key. Place it in the cloned directory's root.

##
<b> This is NOT a commercial product. The OpenAI logo mixed with the style of the 'Terminal' MacOS app icon in the image at top is used to convey the fact that the API keys used are official, according to fair use. </b>
