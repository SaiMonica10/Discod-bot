# 🤖 Discord AI Chatbot (Cohere + Python)

A simple **AI-powered Discord chatbot** built using **Python**, **discord.py**, and the **Cohere API**.
The bot reads messages in a Discord channel and responds using an AI language model.

---

## 🚀 Features

* AI-powered responses using Cohere
* Built with `discord.py`
* Responds to user messages automatically
* Simple and beginner-friendly code
* Easy to extend with new commands

---

## 🧰 Technologies Used

* Python 3
* discord.py
* Cohere AI API

---

## 📂 Project Structure

```
python_project/
│
├── bot.py          # Main Discord bot script
├── README.md       # Project documentation
└── .venv/          # Virtual environment (not required in repo)
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/discord-ai-bot.git
cd discord-ai-bot
```

---

### 2️⃣ Create a virtual environment

Mac / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install discord.py
pip install cohere
```

---

## 🔑 Setup API Keys

You need two things:

### 1️⃣ Discord Bot Token

1. Go to the Discord Developer Portal
2. Create a new application
3. Add a **Bot**
4. Copy the **Bot Token**

Enable **Message Content Intent** in the bot settings.

---

### 2️⃣ Cohere API Key

Create an API key from:

https://dashboard.cohere.com/api-keys

---

## 🧠 Configure the Bot

Open **bot.py** and replace:

```python
self.cohere = cohere.Client("YOUR_COHERE_API_KEY")
```

and

```python
client.run("YOUR_DISCORD_BOT_TOKEN")
```

with your actual keys.

---

## ▶️ Run the Bot

```bash
python3 bot.py
```

If everything works, you should see:

```
Logged on as your_bot_name!
```

---

## 💬 Usage

Type a message in your Discord server and the bot will reply with an AI-generated response.

Example:

User:

```
hello bot
```

Bot:

```
Hello! How can I help you today?
```

---

## 🛠 Future Improvements

* Conversation memory
* Slash commands
* Better error handling
* Personality customization
* Hosting the bot 24/7

---

## 📜 License

This project is open source and available under the **MIT License**.

---

## 👨‍💻 Author

Created by **[Your Name]**

Feel free to fork, improve, and build your own Discord bots!
