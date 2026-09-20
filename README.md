# Chess Cheat

A small terminal tool that uses Stockfish to recommend chess moves while you enter your opponent's moves.

## Requirements

- Python 3.10 or newer
- The `python-chess` package
- A local Stockfish executable

Install the Python dependency:

```powershell
pip install chess
```

## Setup

Open `chess_cheat.py` and set `STOCKFISH_PATH` to the location of your Stockfish executable.

## Run

```powershell
python chess_cheat.py
```

Choose `w` or `b` when prompted. Enter the opponent's moves in UCI format, such as `e7e5` or `g8f6`. Type `quit` to stop.

## Note

Use this only for personal analysis or where computer assistance is allowed. Do not use it to gain an unfair advantage in live or rated games.