from telethon import TelegramClient

api_id = 36328695
api_hash = '445f15fd27548155a4b40e9b12752167'

client = TelegramClient('minha_sessao', api_id, api_hash)

client.start()

print("Telegram conectado com sucesso!")
print("Você pode fechar esta janela com Ctrl+C")

client.run_until_disconnected()