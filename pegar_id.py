from telethon.sync import TelegramClient

api_id = 36328695
api_hash = "445f15fd27548155a4b40e9b12752167"

with TelegramClient("sessao", api_id, api_hash) as client:
    for dialog in client.get_dialogs():
        print(dialog.name, dialog.id)