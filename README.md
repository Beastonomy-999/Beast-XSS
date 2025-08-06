
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
🔩 Sample Usage (Screenshot Style)
bash
(kali㉿kali)-[~/BEAST-XSS]
$ python3 main.py --url "http://testphp.vulnweb.com/listproducts.php?cat=1" --payloads payloads/basic.txt
Launching BEAST XSS …
or
bash
(kali㉿kali)-[~/BEAST-XSS]
$ python3 main.py --list targets.txt --payloads payloads/dom-based.txt
Launching BEAST XSS …

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
