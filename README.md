# chatGPT clone

[image-1]

A proof-of-concept project on how to build an <b>interactive CLI for chatGPT</b> queries through their own API, based on a video by Warp: https://www.youtube.com/watch?v=7p7kJvckrFE

Few changes were made to the original code to allow for correct formatting, subsequent questions without the code breaking up and some minorly customised output lines.

## INSTRUCTIONS
# Use instructions

Once cloned, by accessing the directory chatGPT 3.5turbo (by default), it can be queried with `python main.py -t "_____________"`, adding your query between quote marks.

The `python main.py --help` command allows to access the help window with further commands.

[image-3]

One could also implement an alias for `python main.py` in their own <b>.zshrc</b> file –or the configuration file of their shell of choice. Obviously also adapt it to the python path set in the source file (<i>e.g.</i> python3).

### API key instructions
To use this, you have to first get your own API key from OpenAI.

[image-2]

Then create a <bi>.env</bi> file with this line: `OPENAI_KEY="____"` filling it with your own API key. Place it in the cloned directory's root.