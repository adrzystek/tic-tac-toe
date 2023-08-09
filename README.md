# tic-tac-toe

Travel-time development project based on Real Python article [Build a Tic-Tac-Toe Game Engine With
an AI Player in Python](https://realpython.com/tic-tac-toe-ai-python/).

## Key features

* front-end-agnostic reusable tic-tac-toe library
* two artificial computer players to play with (a random one and an unbeatable one)
* simple AI implementation based on the minimax algorithm
* object-oriented design with elements of the functional paradigm
* text-based console front-end
* written in Python 3.11, taking advantage of its latest enhancements

## Usage

```
# make sure `python` is Python 3.11
python -m venv venv
source venv/bin/activate

python -m pip install library/
cd frontends/
python -m console -X PLAYER_PLAYING_CROSSES -O PLAYER_PLAYING_NAUGHTS
```

Possible values for `PLAYER_PLAYING_CROSSES` and `PLAYER_PLAYING_NAUGHTS`:
* `human` - player controlled by human
* `minimax` - player making moves based on the minimax algorithm (can't lose!)
* `random` - player making moves at random
