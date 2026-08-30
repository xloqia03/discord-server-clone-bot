<div align="center">

<img src="Habab-Clone-Bot.jpg" alt="Habab Clone Bot" width="220">

# 🛡️ Habab Clone Bot

### Advanced Discord bot engineered for automated Discord server structure replication and strict security access control.

[![Discord](https://img.shields.io/badge/Discord-Habab%20Agency-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/hababagency)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Security](https://img.shields.io/badge/SECURITY-HIGH-red?style=for-the-badge&logo=shield&logoColor=white)]()
[![Status](https://img.shields.io/badge/STATUS-ACTIVE-success?style=for-the-badge)]()

<br>

**Secure replication • Absolute protection**

</div>

---

## ✨ About

**Habab Clone Bot** is a secure, high-performance utility designed to replicate Discord server structures, including categories, text channels, voice channels, roles, and permission hierarchies, while providing authorization and security controls against unauthorized access.

### Features

- 🔄 Full server structure replication
- 👥 Role replication and permission mapping
- 📁 Category replication
- 💬 Text channel replication
- 🔊 Voice channel replication
- 🔒 Strict authorization protection
- ⚡ Security alerts to the owner's DM
- 🛡️ Permission validation
- 🤖 Modern slash command interface
- 📝 Detailed terminal logging
- 🌐 Environment-based token management

---

## 🎧 Highlights

### 🛡️ Core Protection Shield

The bot integrates security checks designed to prevent unauthorized cloning attempts.

Unauthorized requests can be blocked and security events can be logged and reported to the configured owner.

### 🔄 Precise Hierarchy Replication

The replication engine maps roles, categories, channels, and permission overwrites to reproduce the source server structure accurately.

---

## 🚀 Commands

### 🔄 Clone Server

```text
/clone source_guild_id:<TARGET_SERVER_ID>
```

Starts the server replication process after authorization and security validation.

---

## 🧠 Architecture

```text
Discord Slash Command
        │
        ▼
 Security Validation
        │
        ├─► [Authorized]
        │          │
        │          ▼
        │   Structure Fetcher
        │          │
        │          ▼
        │   Role Replication
        │          │
        │          ▼
        │   Channel Replication
        │
        └─► [Unauthorized]
                   │
                   ▼
             Security Alert
                   │
                   ▼
              Block Request
```

---

## 📁 Project Structure

```text
discord-server-clone-bot/
│
├── bot.py
├── config.py
├── .env
├── Habab-Clone-Bot.jpg
├── requirements.txt
├── venv/
├── .gitignore
└── README.md
```

---

## 🛠️ Requirements

- Python 3.x
- Discord Bot Token
- Required Discord permissions
- Required Gateway Intents
- Internet access for Discord API communication
- Linux / WSL environment recommended

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/xloqia03/discord-server-clone-bot.git
```

Enter the project directory:

```bash
cd discord-server-clone-bot
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file:

```env
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
OWNER_ID=YOUR_DISCORD_USER_ID
```

Replace the placeholder values with your own configuration.

> ⚠️ Never publish your real Discord bot token.

---

## ⚡ Running the Bot

From the project directory:

```bash
source venv/bin/activate
```

Then start the bot:

```bash
python bot.py
```

---

## 🔒 Security

Security is a core part of the project.

The bot is designed to:

- Validate command authorization
- Validate the execution context
- Protect configured servers
- Block unauthorized requests
- Log security events
- Send owner notifications when configured
- Keep sensitive configuration inside environment variables

### Never expose your token

Do **not** commit `.env` or your real Discord token to GitHub.

Recommended `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## 🛡️ Execution Lifecycle

1. The bot starts and connects to Discord.
2. Slash commands are registered.
3. A user executes `/clone`.
4. The bot validates the executor.
5. The bot validates the requested server context.
6. Unauthorized requests are blocked.
7. Security events are logged.
8. Authorized requests continue to the replication engine.
9. Roles are processed and mapped.
10. Categories are recreated.
11. Text and voice channels are recreated.
12. Permission overwrites are applied where supported.
13. The replication process completes.

---

## 📊 Replication Scope

| Component | Supported |
|---|:---:|
| Roles | ✅ |
| Role Permissions | ✅ |
| Categories | ✅ |
| Text Channels | ✅ |
| Voice Channels | ✅ |
| Channel Permissions | ✅ |
| Permission Overwrites | ✅ |
| Server Structure | ✅ |

> Actual capabilities depend on the implementation in the current bot version and Discord API permissions.

---

## 🧩 Permissions

The bot requires sufficient Discord permissions to perform the operations enabled by the implementation.

For reliable server structure management, the bot may require permissions such as:

```text
Manage Roles
Manage Channels
View Channels
Send Messages
Embed Links
Read Message History
```

Only grant the permissions required by your deployment.

---

## 🧪 Development

Activate the virtual environment:

```bash
source venv/bin/activate
```

Run the bot:

```bash
python bot.py
```

Check the terminal output for startup and security logs.

---

## 📝 Logging

The bot can provide terminal logging for:

- Bot startup
- Command execution
- Authorization checks
- Security events
- Role processing
- Channel processing
- Replication status
- Errors and exceptions

Example:

```text
[INFO] Bot starting...
[INFO] Connected to Discord
[INFO] Slash commands loaded
[INFO] Clone request received
[SECURITY] Authorization validated
[CLONE] Processing server structure
[CLONE] Replication completed
```

---

## 🎯 Roadmap

- [ ] Multi-server batch cloning
- [ ] Advanced permission filtering
- [ ] Improved role hierarchy handling
- [ ] Better channel overwrite mapping
- [ ] Web-based management dashboard
- [ ] Automated backup schedules
- [ ] Extended security audit logging
- [ ] Configurable replication profiles
- [ ] Detailed replication progress reporting
- [ ] Error recovery and rollback support

---

## 🌐 Community & Support

### Discord

**Habab Agency Community**

https://discord.gg/hababagency

### GitHub

**@xloqia03**

https://github.com/xloqia03

---

## 📜 Disclaimer

This project is intended for legitimate server administration, migration, backup, testing, and development purposes.

Only replicate servers and structures that you are authorized to manage or reproduce.

Always follow Discord's Terms of Service and API policies.

---

<div align="center">

### 🛡️ Habab Clone Bot

**Secure replication • Absolute protection**

Made with ❤️ for secure Discord server management.

</div>
