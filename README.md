# Oreca OSINT v2.0

> **Advanced Open-Source OSINT Information Gathering Tool**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS%20%7C%20Android%20%7C%20iOS-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Tools Overview](#-tools-overview)
- [Supported Systems](#-supported-systems)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Features

✅ **User-Friendly Interface** - Interactive and easy-to-use menus  
✅ **Multi-Platform Support** - Windows, Linux, macOS, Termux, Android  
✅ **Advanced Tools** - 15+ professional information gathering tools  
✅ **Optimized Performance** - Fast and efficient data processing  
✅ **Robust Error Handling** - Clear error messages and solutions  
✅ **Colorful Output** - Attractive and readable interface  
✅ **High Reliability** - High success rate in queries  
✅ **Cross-Platform** - Works on desktop and mobile platforms  

---

## 📦 Requirements

### Python Version
- Python 3.6 or higher

### Required Libraries
```
requests          # HTTP requests library
phonenumbers      # Phone number parsing and validation
```

### System Requirements
- Internet connection
- 10 MB disk space
- 100 MB RAM minimum

---

## 🚀 Installation

### Linux / Kali Linux / macOS

```bash
# Clone the repository
git clone https://github.com/blackevil518/Oreca_osint
cd Oreca_osint

# Make install script executable
chmod +x install.sh

# Run installation
./install.sh

# Start the tool
python3 oreca.py
```

### Windows

```bash
# Clone the repository
git clone https://github.com/blackevil518/Oreca_osint
cd Oreca_osint

# Run installation script
install.bat

# Start the tool
python oreca.py
```

### Termux (Android/iPhone)

```bash
# Update Termux
apt update && apt upgrade

# Install Python
apt install python3 pip git

# Clone repository
git clone https://github.com/blackevil518/Oreca_osint
cd Oreca_osint

# Install requirements
pip install -r requirements.txt

# Start the tool
python3 oreca.py
```

### Manual Installation

```bash
# Install dependencies manually
pip3 install requests phonenumbers

# Run directly
python3 oreca.py
```

---

## 📖 Usage

### Quick Start

```bash
python3 oreca.py
```

### Step-by-Step Guide

1. **Select Your Platform**
   ```
   1/k) Kali Linux / Windows / Mac
   2/p) iPhone / Android / Mobile
   ```

2. **Choose Tool Category**
   - User Information Collection
   - Website Information Gathering

3. **Select Specific Tool**
   - Search Email
   - Phone Number Lookup
   - Username Search
   - IP Address Information
   - Website Info
   - Subdomain Extraction
   - Link Extraction
   - Port Scanner

4. **Enter Required Data**

5. **Get Results**

---

## 🛠️ Tools Overview

### User Information Gathering Tools

#### 1. **Email Search** 🔍
Search for email addresses across 15+ services and platforms

**What it does:**
- Checks if email is linked to various online services
- Searches across: Microsoft, Apple, Google, Meta, Twitter, Instagram, TikTok, Snapchat, SoundCloud, Noon, Acaps, Connected, NewsAPI, DarkWebID, Adobe, NewYorker, Talabat
- Provides account status (Linked ✅ or Not Found ❌)
- Shows comprehensive results in organized format

**How to use:**
```
1. Run the tool: python3 oreca.py
2. Select platform: 1 (Kali/Windows/Mac)
3. Select tool category: 1 (User Information)
4. Select tool: 1 (Search Email)
5. Enter email: user@example.com
6. View results immediately
```

**Usage Example:**
```
Enter Email: john@gmail.com
↓
[*] Searching for john@gmail.com...
↓
[+] Email linked to Microsoft Account ☑️
[+] Email linked to Instagram ☑️
[-] Not linked on Facebook ✖️
[+] Email linked to Twitter ☑️
↓
[+] Summary: Found on 3 services
```

**Advantages:**
- Checks multiple platforms simultaneously
- Accurate results
- Fast response time
- Useful for account verification
- Helps find linked social profiles

**Services Checked:**
1. Microsoft/Outlook
2. Apple iCloud
3. Facebook
4. Twitter
5. Instagram
6. TikTok
7. Snapchat
8. SoundCloud
9. Noon.com
10. Acaps.org
11. Connected.com
12. NewsAPI
13. DarkWebID
14. Adobe
15. NewYorker

---

#### 2. **Phone Number Lookup** 📱
Extract detailed information about phone numbers

**What it does:**
- Identifies phone number owner name
- Shows country and carrier information
- Extracts phone type (Mobile/Landline)
- Searches multiple databases
- Supports 25+ country codes

**How to use:**
```
1. Run the tool: python3 oreca.py
2. Select platform: 1 (Kali/Windows/Mac)
3. Select tool category: 1 (User Information)
4. Select tool: 2 (Phone Number Lookup)
5. Enter phone: country_code phone_number (e.g., 974 52947429)
6. View detailed information
```

**Usage Example:**
```
Enter Phone Number: 974 52947429
↓
[+] Phone Information:
[+] Number: 974 52947429
[+] Country: Qatar
[+] Name: Ahmed Mohammed
[+] Carrier: Ooredoo
[+] Type: Mobile
```

**Supported Countries:**
```
Egypt (20)          Iran (98)           Morocco (212)
Algeria (213)       Tunisia (216)       Sudan (249)
Somalia (252)       Lebanon (961)       Jordan (962)
Syria (963)         Iraq (964)          Kuwait (965)
Saudi Arabia (966)  Yemen (967)         Oman (968)
Palestine (970)     UAE (971)           Israel (972)
Bahrain (973)       Qatar (974)         USA (1)
Canada (1)          UK (44)             Germany (49)
France (33)         Spain (34)          Italy (39)
```

**Advantages:**
- Finds phone owner information
- Identifies carrier
- Useful for verification
- Helps detect spam numbers
- Shows number type

---

#### 3. **Username Search** 👤
Search for usernames across 28+ social media platforms

**What it does:**
- Searches across popular social networks
- Checks availability on multiple platforms
- Provides direct profile links
- Instant results

**How to use:**
```
1. Run the tool: python3 oreca.py
2. Select platform: 1 (Kali/Windows/Mac)
3. Select tool category: 1 (User Information)
4. Select tool: 3 (Username Search)
5. Enter username: john_doe
6. View found profiles
```

**Usage Example:**
```
Enter username: john_doe
↓
[*] Searching for @john_doe...
↓
[+] Found on Instagram: https://www.instagram.com/john_doe
[+] Found on Twitter: https://twitter.com/john_doe
[+] Found on GitHub: https://github.com/john_doe
[+] Found on Reddit: https://reddit.com/u/john_doe
[-] Not found on Facebook
↓
[+] Summary: Found on 4 platforms
```

**Platforms Searched:**
```
Instagram       TikTok          Twitter         Telegram
Snapchat        GitHub          Reddit          LinkedIn
Discord         YouTube         Twitch          Pinterest
Quora           Stack Overflow  Medium          Dev.to
Behance         Dribbble        Codecademy      HackerRank
CodeWars        Codepen         Patreon         OnlyFans
Mastodon        Bluesky         Threads         Medium
```

**Advantages:**
- Find multiple profiles at once
- Verify username availability
- Collect user information
- Identify connected accounts
- Useful for social engineering assessment

---

#### 4. **IP Address Information** 🌍
Get comprehensive information about IP addresses

**What it does:**
- Determines geographic location (country, city)
- Shows timezone information
- Identifies ISP/Organization
- Provides latitude and longitude
- Shows ASN (Autonomous System Number)

**How to use:**
```
1. Run the tool: python3 oreca.py
2. Select platform: 1 (Kali/Windows/Mac)
3. Select tool category: 1 (User Information)
4. Select tool: 4 (IP Address Info)
5. Enter IP address: 8.8.8.8
6. View geographic information
```

**Usage Example:**
```
Enter IP address: 8.8.8.8
↓
[+] IP Information:
[+] IP Address: 8.8.8.8
[+] Country: United States
[+] City: Mountain View
[+] Timezone: America/Los_Angeles
[+] ISP: Google LLC
[+] Latitude: 37.4220
[+] Longitude: -122.0842
[+] ASN: AS15169
```

**Information Provided:**
```
Geographic:
  - Country
  - City
  - Coordinates (Latitude/Longitude)
  - Timezone

Network:
  - ISP/Organization
  - ASN (Autonomous System Number)
  - Connection Type
  - Domain
```

**Advantages:**
- Track IP locations
- Identify ISP information
- Verify server locations
- Useful for security analysis
- Helps detect proxies/VPNs

---

### Website Information Gathering Tools

#### 1. **Website Information** 🌐
Gather WHOIS and domain information

**What it does:**
- Retrieves domain registration details
- Shows domain age
- Displays creation, update, and expiration dates
- Identifies website IP address
- Shows server information

**How to use:**
```
1. Run the tool: python3 oreca.py
2. Select platform: 1 (Kali/Windows/Mac)
3. Select tool category: 2 (Website Info)
4. Select tool: 1 (Basic Info)
5. Enter website: www.example.com
6. View domain information
```

**Usage Example:**
```
Enter website link: www.google.com
↓
[+] Website Information:
[+] Domain: google.com
[+] Age: 25 years
[+] Country: United States
[+] Created: 1998-09-15
[+] Updated: 2024-05-20
[+] Expires: 2028-09-15
[+] Website IP: 142.250.185.46
[+] Server IP: 142.250.185.46
```

**Information Retrieved:**
```
Domain Details:
  - Registration date
  - Expiration date
  - Last update date
  - Domain age
  - Registrar

Server Info:
  - IP Address
  - Server location
  - Organization
  - ISP
```

**Advantages:**
- Find domain owner info
- Check domain expiration
- Identify server location
- Useful for competitor analysis
- Helps assess website legitimacy

---

#### 2. **Subdomain Extraction** 🔗
Find all subdomains for a target domain

**What it does:**
- Enumerates subdomains using online APIs
- Uses Sonar.omnisint.io database
- Provides comprehensive subdomain list
- Helps identify infrastructure

**How to use:**
```
1. Run the tool: python3 oreca.py
2. Select platform: 1 (Kali/Windows/Mac)
3. Select tool category: 2 (Website Info)
4. Select tool: 2 (Extract Subdomains)
5. Enter website: example.com
6. View all found subdomains
```

**Usage Example:**
```
Enter website link: google.com
↓
[*] Fetching subdomains...
↓
[+] Found 45 subdomains:
[+] www.google.com
[+] mail.google.com
[+] drive.google.com
[+] maps.google.com
[+] photos.google.com
[+] scholar.google.com
[+] play.google.com
[+] analytics.google.com
[+] adwords.google.com
... and 36 more
```

**Common Subdomains Found:**
```
www             mail            ftp
blog            admin           api
cdn             upload          download
store           support         help
mail            smtp            pop
dev             staging         test
staging         beta            preview
backup          assets          images
```

**Advantages:**
- Identify all web services
- Find hidden services
- Discover administrative panels
- Useful for penetration testing
- Map target infrastructure

---

#### 3. **Link Extraction** 🔍
Extract all links from a website

**What it does:**
- Parses website HTML
- Extracts all href links
- Removes fragments (#)
- Provides complete list of URLs

**How to use:**
```
1. Run the tool: python3 oreca.py
2. Select platform: 1 (Kali/Windows/Mac)
3. Select tool category: 2 (Website Info)
4. Select tool: 3 (Extract Links)
5. Enter website: www.example.com
6. View extracted links
```

**Usage Example:**
```
Enter website link: www.example.com
↓
[*] Extracting links...
↓
[+] Found 47 links:
[+] https://example.com/about
[+] https://example.com/contact
[+] https://example.com/products
[+] https://example.com/blog
[+] https://cdn.example.com/style.css
[+] https://api.example.com/v1/users
... and 41 more
```

**Link Types Found:**
```
Internal Links:
  - Main pages
  - Product pages
  - Blog posts
  - Contact forms

External Links:
  - CDN resources
  - External services
  - Analytics
  - Social media
```

**Advantages:**
- Map website structure
- Find internal pages
- Discover API endpoints
- Identify external services
- Useful for SEO analysis

---

#### 4. **Port Scanner** 🔓
Scan for open ports on target host

**What it does:**
- Scans common ports (1-1024)
- Identifies open ports
- Shows service status
- Helps in security assessment

**How to use:**
```
1. Run the tool: python3 oreca.py
2. Select platform: 1 (Kali/Windows/Mac)
3. Select tool category: 2 (Website Info)
4. Select tool: 4 (Port Scanner)
5. Enter website: www.example.com
6. Monitor scan progress
7. View open ports
```

**Usage Example:**
```
Enter website link: google.com
↓
[*] Starting port scan on 142.250.185.46...
↓
[*] Scanning... Port: 1
[*] Scanning... Port: 22
[*] Scanning... Port: 80
[+] Open port found: 80 (HTTP)
[*] Scanning... Port: 443
[+] Open port found: 443 (HTTPS)
[*] Scanning... Port: 3306
[*] Scanning... Port: 8080
↓
[+] Scan complete! Open ports: [80, 443]
```

**Common Ports Checked:**
```
20      FTP Data
21      FTP Control
22      SSH
25      SMTP
53      DNS
80      HTTP
110     POP3
143     IMAP
443     HTTPS
3306    MySQL
5432    PostgreSQL
5672    AMQP
6379    Redis
8080    HTTP Proxy
8443    HTTPS Proxy
```

**Advantages:**
- Identify exposed services
- Find potential vulnerabilities
- Assess security posture
- Discover attack surfaces
- Useful for security audits

---

## 💻 Supported Systems

| System | Version | Support | Status |
|--------|---------|---------|--------|
| **Linux** | All | ✅ Full | Ready |
| **Kali Linux** | All | ✅ Full | Ready |
| **Windows** | 7, 8, 10, 11 | ✅ Full | Ready |
| **macOS** | 10.9+ | ✅ Full | Ready |
| **Termux** | Android/iPhone | ✅ Full | Ready |
| **Ubuntu** | All | ✅ Full | Ready |
| **Debian** | All | ✅ Full | Ready |
| **CentOS** | All | ✅ Full | Ready |

---

## 📋 Examples

### Example 1: Email Search

```bash
$ python3 oreca.py

Select platform: 1

Select tool: 1 (User Information)

Select search type: 1 (Search Email)

Enter Email: john@gmail.com

[+] Searching for john@gmail.com...

[+] Email linked to Microsoft Account ☑️
[+] Email linked to Instagram ☑️
[-] Not linked on Facebook ✖️
[+] Email linked to Twitter ☑️

[+] Summary: Found on 3 services
```

### Example 2: Phone Lookup

```bash
$ python3 oreca.py

Select platform: 1

Select tool: 1 (User Information)

Select search type: 2 (Phone Lookup)

Enter Phone Number: 974 52947429

[+] Phone Information:
[+] Number: 974 52947429
[+] Country: Qatar
[+] Name: Ahmed Mohammed
[+] Carrier: Ooredoo
```

### Example 3: Username Search

```bash
$ python3 oreca.py

Select platform: 1

Select tool: 1 (User Information)

Select search type: 3 (Username Search)

Enter username: blackevil518

[+] Searching for @blackevil518...

[+] Found on Instagram: https://www.instagram.com/blackevil518
[+] Found on Twitter: https://twitter.com/blackevil518
[+] Found on GitHub: https://github.com/blackevil518
[+] Found on Telegram: https://t.me/blackevil518

[+] Summary: Found on 4 platforms
```

### Example 4: Website Information

```bash
$ python3 oreca.py

Select platform: 1

Select tool: 2 (Website Information)

Select search type: 1 (Website Info)

Enter website link: www.example.com

[+] Website Information:
[+] Domain: example.com
[+] Age: 15 years
[+] Country: United States
[+] Created: 2009-01-15
[+] Updated: 2024-05-20
[+] Expires: 2025-01-15
[+] IP Address: 93.184.216.34
```

### Example 5: IP Address Lookup

```bash
$ python3 oreca.py

Select platform: 1

Select tool: 1 (User Information)

Select search type: 4 (IP Information)

Enter IP address: 8.8.8.8

[+] IP Information:
[+] IP Address: 8.8.8.8
[+] Country: United States
[+] City: Mountain View
[+] Timezone: America/Los_Angeles
[+] ISP: Google LLC
[+] Latitude: 37.4220
[+] Longitude: -122.0842
```

---

## 🔧 Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'requests'"**
```bash
pip3 install -r requirements.txt
```

**"Permission denied" (Linux/Mac)**
```bash
chmod +x oreca.py
python3 oreca.py
```

**"Connection timeout"**
- Check internet connection
- Wait a few seconds
- Try again

**"Invalid URL"**
- Use correct format: www.example.com
- Don't include spaces
- Ensure domain is valid

**"Python not found" (Windows)**
- Install Python 3.6+
- Enable "Add Python to PATH"
- Restart computer

For more troubleshooting, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## 📊 Project Statistics

```
Total Tools: 8
Email Services Checked: 15+
Social Platforms Searched: 28+
Supported Countries: 25+
Supported Systems: 6+
Code Lines: 800+
```

---

## 🔐 Security & Disclaimer

⚠️ **IMPORTANT**

This tool is provided for **educational and authorized security testing purposes only**.

**Legally:**
- Use only with explicit written permission
- Comply with all local laws
- Don't use for unauthorized access
- Unauthorized use may be illegal

**Responsibility:**
- The author is NOT responsible for misuse
- Users are fully responsible for their actions
- Always get proper authorization
- Use ethically and responsibly

---

## 🤝 Contributing

We welcome contributions! Here's how:

### Report Bugs
- Create an issue on GitHub
- Include error message and steps to reproduce
- Provide system information

### Suggest Features
- Describe the feature clearly
- Explain why it would be useful
- Provide implementation ideas

### Submit Code
```bash
# 1. Fork the repository
# 2. Create feature branch
git checkout -b feature/YourFeature

# 3. Commit changes
git commit -m "Add YourFeature"

# 4. Push to branch
git push origin feature/YourFeature

# 5. Create Pull Request
```

---

## 📞 Support & Contact

- **Telegram:** [@blackevil518](https://t.me/blackevil518)
- **GitHub Issues:** [Report Issues](https://github.com/blackevil518/Oreca_osint/issues)

---

## 📜 Changelog

### v2.0.0 (Current)
- ✅ Complete code rewrite
- ✅ Full Termux/Android support
- ✅ Multi-platform compatibility
- ✅ Improved error handling
- ✅ Better UI/UX
- ✅ Performance optimization
- ✅ Comprehensive documentation

### v1.0.0
- Initial release

---

## 📄 License

This project is licensed under the MIT License

---

## 🙏 Credits

- Security community
- All contributors
- Supportive users
- Open-source community

---

<div align="center">

**Made with ❤️ by BLACK EVIL**

⭐ If you find this useful, please give it a star!

[Follow on Telegram](https://t.me/blackevil518) | [Star on GitHub](https://github.com/blackevil518/Oreca_osint)

</div>
