import discord
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('questions.db')

# Create a table to store questions
conn.execute('''CREATE TABLE IF NOT EXISTS questions
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             author TEXT,
             question TEXT);''')

class MyClient(discord.Client):
    async def on_message(message):
        if message.author == client.user:
            return

        # Check if the message is a question
        if message.content.endswith('?'):
            # Store the question and its author in the database
            author = message.author.name
            question = message.content
            conn.execute("INSERT INTO questions (author, question) VALUES (?, ?)", (author, question))
            conn.commit()
            # print("Question recorded:", question)
            print(f'Question from {message.author}: {message.content} *Recorded*')
    
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('your_token_here')
