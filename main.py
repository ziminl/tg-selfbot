from telethon import TelegramClient, events

#https://my.telegram.org/apps
api_id = 
api_hash = ''

client = TelegramClient('user', api_id, api_hash).start()

# This message can contain any text, links, and emoji:
message = "Hello! Thank you for contacting me 👍\nI'll be back soon and reply to your message."

@client.on(events.NewMessage())
async def handler(event):
	sender = await event.get_input_sender()
	await client.send_message(sender, message, file="1.png")
	await client.send_message(sender, message)

client.run_until_disconnected()
