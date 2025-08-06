
# 🛡️ BEAST XSS

BEAST XSS is an advanced, weaponized XSS detection and exploitation tool built for professionals and learners in web security.

## 🔥 Features

- ⚔️ Supports single domain and URL list scans
- 💥 Manual payload control from categorized folders (`/payloads`)
- 👁️ Custom terminal banner (Skull / Roman Reigns optional)
- ⚡ Fast, reliable scanning engine with encoded injection
- 🎯 Curated payloads (basic, DOM-based, obfuscated, etc.)

---
## 🚀 Installation

```bash
# Clone the repo
git clone https://github.com/Beastonomy-999/BEAST-XSS.git

# Change directory
cd BEAST-XSS

# Install dependencies
pip install -r requirements.txt

## 🚀 Usage
**Mode A - Scan Single URL**
```bash
python3 beast_xss.py --url "https://example.com/search?q=test"

**Mode B - Scan List of URLs from File**
```bash
python3 beast_xss.py --list url_list.txt

```

## 📁 Payload Structure
- `basic.txt`: General XSS payloads
- `dom_based.txt`: DOM-based attack vectors
- `obfuscated.txt`: Bypassing WAFs & filters
- `polyglots.txt`: Complex cross-context payloads

## 👨‍💻 Built For
- Ethical Hackers
- Bug Bounty Hunters
- Red Teams & Learners

## 👑 Acknowledge the Beast.
<p align="center">
  <img src="banner.png" alt="BEAST-XSS Logo" width="500px">
</p>

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
