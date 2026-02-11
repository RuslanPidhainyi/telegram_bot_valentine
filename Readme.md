# Telegram Valentine Bot

## Requirements
Python 3.12.0 (Windows).

## Setup and Run (Windows / PowerShell)
Open PowerShell in the project folder and create a virtual environment: 

`py -m venv .venv`. 

If PowerShell blocks script execution (error: “running scripts is disabled on this system”), run: 

`Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

then close PowerShell and open it again. 

Activate the virtual environment: 

`.\.venv\Scripts\Activate.ps1` 

(you should see `(.venv)` in the terminal). 

Install dependencies: 

`py -m pip install --upgrade pip` 

and then 

`py -m pip install -r requirements.txt` 

(if you don’t have `requirements.txt`, install manually: `py -m pip install python-telegram-bot python-dotenv yfinance aiohttp`). 

Create a `.env` file in the project root (same folder as `bot.py`) and set your Telegram bot access token, e.g. `TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN`. 

Also create an `assets` folder in the project root and place your Valentine image there as `assets/valentine.png` (the filename must be exactly `valentine.png`). 

Start the bot with: 

`python bot.py`. 

To stop the bot press **Ctrl + C**. 

To deactivate the virtual environment run: 

`deactivate`.
