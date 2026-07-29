<img width="1115" height="609" alt="image" src="https://github.com/user-attachments/assets/05fa4f4c-77f4-4219-a5ec-809d165aedd0" />

# Brix Tools

![Version](https://img.shields.io/badge/version-1.0.0-gray?style=flat-square)
![Python](https://img.shields.io/badge/python-3.11%2B-gray?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-gray?style=flat-square)

> A modular multi-tool for Discord and network utilities with a sleek gray-scale terminal interface.

---

## 📜 Disclaimer / Avertissement

**EN:** This tool is provided for **educational and research purposes only**. The developers are not responsible for any misuse or damage caused by this software. Users are solely responsible for complying with all applicable local, state, and federal laws. Unauthorized access to computer systems, Discord accounts, or networks without permission is illegal. Do not use this tool for any activity that violates Discord's Terms of Service or any other platform's terms.

**FR:** Cet outil est fourni **uniquement à des fins éducatives et de recherche**. Les développeurs ne sont pas responsables de toute utilisation abusive ou des dommages causés par ce logiciel. Les utilisateurs sont seuls responsables du respect de toutes les lois locales, étatiques et fédérales applicables. L'accès non autorisé à des systèmes informatiques, comptes Discord ou réseaux sans permission est illégal. N'utilisez pas cet outil pour des activités qui violent les conditions d'utilisation de Discord ou de toute autre plateforme.

---

## ✨ Features / Fonctionnalités

### Discord Tools / Outils Discord
| # | Tool / Outil | Description |
|---|---|---|
| 01 | Token Nuker | Delete all servers, friends, DMs from a token |
| 02 | Token Info | Get detailed info from a Discord token |
| 03 | Token Joiner | Join a server with a token |
| 04 | Token Leaver | Leave a server with a token |
| 05 | Token Login | Login via token (browser automation) |
| 06 | Token Server Raid | Mass actions on a server with multiple tokens |
| 07 | Token Spammer | Send messages in bulk with a token |
| 08 | Token Delete Friends | Remove all friends from a token |
| 09 | Token Block Friends | Block all friends from a token |
| 10 | Webhook Delete | Delete a Discord webhook |
| 11 | Webhook Spammer | Spam messages via a webhook |
| 12 | Token Mass DM | Mass DM users with a token |
| 13 | Token Delete DM | Delete all DMs from a token |
| 14 | Token Status Changer | Change online status periodically |
| 15 | Token Language Changer | Change Discord language settings |
| 16 | Token Theme Changer | Toggle light/dark theme |
| 17 | Token Generator | Generate Discord tokens |
| 18 | Bot Server Nuker | Nuke a server with a bot token |
| 19 | Bot Invite To ID | Convert invite code to server ID |
| 20 | Server Info | Get Discord server information |

### Network Tools / Outils Réseau
| # | Tool / Outil | Description |
|---|---|---|
| 21 | IP Pinger | Ping an IP address |
| 22 | IP Lookup | Geolocation and ISP info from an IP |

---

## 📦 Installation

### Prerequisites / Prérequis

- **Python 3.11 or higher** ([Download](https://www.python.org/downloads/))
  - ⚠️ During installation, **check** ✅ **"Add Python to PATH"**
- **Windows 10/11** (recommended), Linux or macOS
- A stable internet connection

### 🔧 Installation Tutorial / Tutoriel d'Installation

#### 🇫🇷 Français

**Étape 1 : Télécharger le projet**
```
Téléchargez et extrayez le dossier Brix-Tools-main.zip
```

**Étape 2 : Ouvrir un terminal dans le dossier**
```bash
cd chemin/vers/Brix-Tools-main
```

**Étape 3 : Lancer l'installation automatique (recommandé)**
```bash
python Setup.bat
```
Cela installe automatiquement tous les modules requis et lance l'outil.

**Étape 4 : Ou installation manuelle**
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Étape 5 : Lancer l'outil**
```bash
lancer le start.bat 
```

#### 🇬🇧 English

**Step 1: Download the project**
```
Download and extract the Brix-Tools-main.zip folder
```

**Step 2: Open a terminal in the folder**
```bash
cd path/to/Brix-Tools-main
```

**Step 3: Run automatic setup (recommended)**
```bash
Launch Setup.bat
```
This installs all required modules and launches the tool.

**Step 4: Or manual installation**
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Step 5: Run the tool**
```bash
Launch Setup.bat
```

---

## 🚀 Usage / Utilisation

1. **Launch the tool** / Lancez l'outil :
   ```bash
   Launch start.bat
   ```
2. **A welcome animation** appears with "WELCOME" ASCII art and a loading bar.
3. **The main menu** displays a centered options box with all tools numbered 01–22.
4. **Type a number** and press Enter to select a tool.
5. **Follow the on-screen prompts** to use the selected tool.

### Controls / Contrôles
- Enter the tool number (e.g., `01`, `21`) and press Enter
- Press `Ctrl+C` to exit a running tool
- Follow terminal prompts for each tool

---

## 🎨 Interface

The entire interface uses a **black and gray gradient** color scheme:
- Menu options are displayed in a bordered box
- All tool interfaces follow the same gray-scale theme
- ASCII art is rendered with per-character animated gradients

---

## 🛠 Requirements / Dépendances

All dependencies are listed in `requirements.txt`. Key packages include:

| Package | Purpose |
|---|---|
| `colorama` | Terminal colors |
| `requests` | HTTP requests (Discord API, webhooks) |
| `selenium` | Browser automation (token login) |
| `discord` | Discord API wrapper (bot tools) |
| `pillow` | Image processing |
| And more... | See `requirements.txt` |

---

## 📁 Project Structure / Structure du Projet

```
Brix-Tools-main/
├── Brix.py                    # Main launcher
├── Setup.py                       # Automatic installer
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── Program/
│   ├── Config/
│   │   ├── Config.py              # Configuration constants
│   │   └── Util.py                # Shared utilities & banners
│   ├── Discord-Token-Nuker.py     # Tool 01
│   ├── Discord-Token-Info.py      # Tool 02
│   ├── ...                        # Tools 03–20
│   └── Ip-Pinger.py               # Tool 21
│   └── Ip-Lookup.py               # Tool 22
```

---

## ⚠️ Important Notes / Notes Importantes

- **Discord tokens** are now entered directly in the terminal (no file needed)
- Some tools require additional setup (e.g., Discord bot token for bot tools)
- Use at your own risk — respect Discord's Terms of Service
- For educational purposes only

---

## 🤝 Contributing / Contribution

This is a personal project. Fork and modify as you wish, but do not resell or claim as your own. / Ceci est un projet personnel. Fork et modifiez comme vous voulez, mais ne revendez pas et ne vous attribuez pas le crédit.

---

*Last updated / Dernière mise à jour : July 2026*
