def send_messages(texts):
    """prints each text and moves text to new list"""
    for message in messages:
        print(message)
        sent_messages.append(message)


sent_messages = []

messages = ['hi', 'how are you?', 'let me know when you get home']

send_messages(messages[:])
print(messages)
print(sent_messages)
