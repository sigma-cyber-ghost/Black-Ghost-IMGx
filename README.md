# 🩸 BLACK-GHOST-IMGx  
**Metadata Obliterator & Stego Forge**  

## 🩸 Overview  
Powerful image sanitization/steganography toolkit for cyber operatives. Wipes digital fingerprints (EXIF/JFIF/comments) and embeds/extracts hidden payloads. Built for Kali Linux, Debian, and Termux.  

## 🩸 Key Features  
| Module                      | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| **Extract Image Metadata**  | Dumps all metadata (EXIF/JFIF) from images                                  |
| **Remove Metadata**         | Wipes EXIF/JFIF traces via ExifTool                                         |
| **Blast Image**             | Irreversible sector wipe with `dd` zero-overwrite                           |
| **Stego-Scanner**           | Extracts hidden payloads using Steghide                                     |
| **Stego-Hide**              | Embeds secret files/messages into images                                    |

## 🩸 Menu  
1. Extract Metadata (ExifTool)  
2. Sanitize Metadata (Remove EXIF/JFIF)  
3. Extreme Sector Purge (dd wipe)  
4. Stego-Scanner (Extract payloads)  
5. Stego-Hide (Embed secrets)  
6. Exit

## 🩸 Installation Linux
```python
apt install python3 python3-pip git coreutils libimage-exiftool-perl steghide -y
pip install pillow rich
git clone https://github.com/sigma-cyber-ghost/Black-Ghost-IMGx.git
cd Black-Ghost-IMGx
python3 black_ghost_imgx.py
```
## 🩸 Installation Termux
```python
pkg update && pkg upgrade -y
pkg install python git coreutils exiftool steghide -y
pip install pillow rich
git clone https://github.com/sigma-cyber-ghost/Black-Ghost-IMGx.git
cd Black-Ghost-IMGx
python3 black_ghost_imgx.py
```
## 🩸 Requirements
Python 3.8+
Kali/Debian/Termux
Dependencies: exiftool, steghide, coreutils, Pillow, rich

## 🩸 This tool is crafted for Black-Hat operatives. Sigma-Ghost, the creator, holds no responsibility for your actions. You own your consequences.

## 🌐 Connect With Us

[![Telegram](https://img.shields.io/badge/Telegram-Sigma_Ghost-blue?logo=telegram)](https://t.me/Sigma_Cyber_Ghost)  [![YouTube](https://img.shields.io/badge/YouTube-Sigma_Ghost-red?logo=youtube)](https://www.youtube.com/@sigma_ghost_hacking)  [![Instagram](https://img.shields.io/badge/Instagram-Safder_Khan-purple?logo=instagram)](https://www.instagram.com/safderkhan0800_/)  [![Twitter](https://img.shields.io/badge/Twitter-@safderkhan0800_-1DA1F2?logo=twitter)](https://twitter.com/safderkhan0800_)
