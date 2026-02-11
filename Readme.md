# need version on pythan 3.12.0

# after need to activate venv

py -m venv .venv

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Potem zamknij i otwórz PowerShell ponownie i aktywuj venv:

.\.venv\Scripts\Activate.ps1

# start bot
python bot.py
