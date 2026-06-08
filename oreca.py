#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oreca OSINT Tool
A comprehensive OSINT collection tool for information gathering
Author: @evil_5188
Website: https://t.me/blackevil518
"""

import os
import sys
import platform
import threading
import socket
import re
import requests
import json
from threading import Thread, Lock
from time import sleep
from random import choice
from requests import get, post
import urllib.parse as urlparse

# Handle different terminal colors based on OS
def setup_colors():
    """Setup color codes based on OS"""
    if platform.system() == "Windows":
        os.system("color")  # Enable ANSI colors on Windows
    
    return {
        'RED': '\033[1;31;40m',
        'YELLOW': '\033[1;33;40m',
        'CYAN': '\033[1;36;40m',
        'GREEN': '\033[1;32;40m',
        'WHITE': '\033[1;37;40m',
        'RESET': '\033[0m'
    }

COLORS = setup_colors()
red = COLORS['RED']
yel = COLORS['YELLOW']
bloFT = COLORS['CYAN']
grn = COLORS['GREEN']
wit = COLORS['WHITE']
reset = COLORS['RESET']

LINX = {"K", "k", "1"}
PHON = {"P", "p", "2"}
PRNT = Lock()
threads = []

# Import phonenumbers with error handling
try:
    import phonenumbers
    from phonenumbers import carrier
    PHONENUMBERS_AVAILABLE = True
except ImportError:
    PHONENUMBERS_AVAILABLE = False

def print_safe(*args, **kwargs):
    """Thread-safe print function"""
    with PRNT:
        print(*args, **kwargs)

def get_user_agent():
    """Generate realistic user agent"""
    ios = ['13_5', '13_6', '14', '13_3', '14_4', '15', '12_6', '15_1', '15_1_1', '14_3', '14_6', '13_2', '12_7']
    rv = ['604.1', '596.2', '706.6', '397.3', '937.9', '936.3']
    version = ['18.5.0', '21.1.0', '19.3.0', '19.1.0', '17.7.0', '16.6.1']
    
    user_agent = f'Mozilla/5.0 (iPhone; CPU iPhone OS {choice(ios)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{choice(version)} Mobile/15E148 Safari/{choice(rv)}'
    return user_agent

def go_back():
    """Go back to menu or exit"""
    mods = input(f'\n{grn}[0]{wit} Back to list <<\n{grn}[1]{wit} Exit <<\n{yel}[$]{wit} Enter: ')
    if mods == '0':
        return settings()
    else:
        print(f'{red}[*] Exiting...{wit}')
        sys.exit(0)

class WebScanner:
    """Website information gathering class"""
    
    def __init__(self, mode):
        self.all_links = []
        self.api = input(f'\n{yel}[?]{wit} Enter the website link: ').strip()
        
        if not self.api:
            print(f'{red}[-] Empty URL provided{wit}')
            return settings()
        
        try:
            self.parse_url()
            
            if mode == '1':
                self.web_info()
            elif mode == '2':
                self.sub_domains()
            elif mode == '3':
                self.extract_links()
            elif mode == '4':
                self.port_scanner()
            else:
                print_safe(f'\t\t{bloFT}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{wit}')
                return settings()
        except Exception as e:
            print(f'{red}[-] Error: {str(e)}{wit}')
            go_back()
    
    def parse_url(self):
        """Parse and validate URL"""
        if 'https://' in self.api:
            self.apis = self.api.split('https://')[1]
        elif 'http://' in self.api:
            self.apis = self.api.split('http://')[1]
        elif 'www' in self.api:
            self.apis = self.api
        else:
            self.apis = f'www.{self.api}'
        
        # Remove trailing slashes
        self.apis = self.apis.rstrip('/')
        self.api = self.apis if self.apis.startswith('www') else f'www.{self.apis}'
        self.web_ip = self.apis.split('.')[0]
        
        try:
            self.ips = socket.gethostbyname(self.api)
            print(f'{grn}[+] IP resolved: {self.ips}{wit}')
        except socket.gaierror:
            print(f'{red}[-] Could not resolve domain{wit}')
            print(f'{red}[-] Please enter a valid link (e.g., www.instagram.com){wit}')
            go_back()
    
    def extract_links(self):
        """Extract links from website"""
        try:
            print(f'{yel}[*] Extracting links...{wit}')
            response = get(f'https://{self.api}', timeout=10, headers={'User-Agent': get_user_agent()})
            links = re.findall(r'(?:href=")([^"]*)', response.content.decode(errors="ignore"))
            
            if not links:
                print(f'{red}[-] No links found{wit}')
            else:
                print(f'{grn}[+] Found {len(links)} links:{wit}')
                for link in links:
                    full_link = urlparse.urljoin(self.api, link)
                    if '#' in full_link:
                        full_link = full_link.split("#")[0]
                    print_safe(f'{grn}[+]{wit} {full_link}')
        except requests.exceptions.RequestException as e:
            print(f'{red}[-] Error extracting links: {str(e)}{wit}')
        finally:
            go_back()
    
    def sub_domains(self):
        """Extract subdomains"""
        try:
            print(f'{yel}[*] Fetching subdomains...{wit}')
            response = get(f'https://sonar.omnisint.io/subdomains/{self.apis}', timeout=10).text
            domains = re.findall(r'"([^"]*)"', response)
            
            if not domains:
                print(f'{red}[-] No subdomains found{wit}')
            else:
                print(f'{grn}[+] Found {len(domains)} subdomains:{wit}')
                for domain in domains[:100]:  # Limit to first 100
                    if domain and domain != self.apis:
                        print_safe(f'{grn}[+]{wit} {domain}')
        except Exception as e:
            print(f'{red}[-] Error: {str(e)}{wit}')
        finally:
            print(f'\t\t{bloFT}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{wit}')
            go_back()
    
    def web_info(self):
        """Get website information"""
        try:
            print(f'{yel}[*] Fetching website information...{wit}')
            headers = {
                'Host': f'{self.web_ip}.com.w3snoop.com',
                'User-Agent': get_user_agent(),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            }
            response = get(f'https://{self.web_ip}.com.w3snoop.com/', headers=headers, timeout=10)
            
            # Extract information using regex
            patterns = {
                'Server IP': r'Server IP Address:<td>(.*?)<',
                'Country': r'Country:<td>(.*?)<br>',
                'Age': r'Age:<td>(.*?)<',
                'Created': r'Domain Created:<td>(.*?)<',
                'Updated': r'Domain Updated:<td>(.*?)<',
                'Expires': r'Domain Expires:<td>(.*?)<'
            }
            
            print(f'\n{grn}{'━' * 50}{wit}')
            print(f'{grn}[+] Website Information:{wit}')
            print(f'{grn}{'━' * 50}{wit}\n')
            
            for label, pattern in patterns.items():
                match = re.findall(pattern, response.text)
                if match:
                    print(f'{grn}[+]{wit} {label}: {match[0].strip()}')
            
            print(f'\n{grn}[+]{wit} Website IP: {self.ips}')
            print(f'\n{grn}{'━' * 50}{wit}\n')
        except Exception as e:
            print(f'{red}[-] Error: {str(e)}{wit}')
        finally:
            go_back()
    
    def port_scanner(self):
        """Scan open ports"""
        print_safe(f'\t\t{bloFT}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{wit}')
        print_safe(f'{yel}[*] Starting port scan on {self.ips}...{wit}')
        
        open_ports = []
        
        for port in range(1, 1025):  # Scan common ports
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex((self.ips, port))
                
                if result == 0:
                    open_ports.append(port)
                    print_safe(f'{grn}[+] Open port found: {port}{wit}')
                else:
                    print_safe(f'\r{yel}[*] Scanning... Port: {port}{wit}', end='')
                
                sock.close()
            except socket.error:
                pass
        
        print_safe(f'\n{grn}[+] Scan complete! Open ports: {open_ports}{wit}\n')
        go_back()

class PhoneSearcher:
    """Phone number information search"""
    
    def __init__(self):
        self.number = input(f'\n{yel}[+]{wit} Enter Phone Number (e.g., 974 52947429): ').strip()
        parts = self.number.split()
        
        if len(parts) < 2:
            print(f'{red}[-] Invalid format. Use: country_code phone_number{wit}')
            go_back()
            return
        
        self.code = parts[0]
        self.phone = parts[1]
        self.number_search()
    
    def get_country_name(self):
        """Get country name from country code"""
        countries = {
            '20': 'Egypt', '98': 'Iran', '212': 'Morocco', '213': 'Algeria',
            '216': 'Tunisia', '249': 'Sudan', '252': 'Somalia', '961': 'Lebanon',
            '962': 'Jordan', '963': 'Syria', '964': 'Iraq', '965': 'Kuwait',
            '966': 'Saudi Arabia', '967': 'Yemen', '968': 'Oman', '970': 'Palestine',
            '971': 'UAE', '972': 'Israel', '973': 'Bahrain', '974': 'Qatar'
        }
        return countries.get(self.code, None)
    
    def number_search(self):
        """Search for number information"""
        country = self.get_country_name()
        
        if not country:
            print(f'{red}[!] Country code not supported yet{wit}')
            go_back()
            return
        
        try:
            # Phone lookup
            response = get(
                f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={self.phone}&country_code={self.code}",
                headers={"User-Agent": get_user_agent()},
                timeout=10
            )
            
            data = response.json()
            if data.get('result'):
                result = data['result'][0]
                print(f'\n{grn}[+] Phone Information:{wit}')
                print(f'{grn}[+]{wit} Number: {result.get("number", "N/A")}')
                print(f'{grn}[+]{wit} Country: {country}')
                print(f'{grn}[+]{wit} Name: {result.get("name", "N/A")}')
                
                if PHONENUMBERS_AVAILABLE:
                    try:
                        pho = phonenumbers.parse(f'+{self.code}{self.phone}')
                        carrier_name = carrier.name_for_number(pho, 'en')
                        print(f'{grn}[+]{wit} Carrier: {carrier_name}')
                    except:
                        pass
            else:
                print(f'{red}[-] No information found{wit}')
        except Exception as e:
            print(f'{red}[-] Error: {str(e)}{wit}')
        finally:
            go_back()

class UsernameSearcher:
    """Search for username across multiple platforms"""
    
    def __init__(self):
        self.username = input(f'{yel}[?]{wit} Enter username: ').strip()
        
        if not self.username:
            print(f'{red}[-] Empty username{wit}')
            go_back()
            return
        
        self.platforms = {
            'Instagram': 'https://www.instagram.com/{}',
            'TikTok': 'https://www.tiktok.com/@{}',
            'Twitter': 'https://twitter.com/{}',
            'Telegram': 'https://t.me/{}',
            'GitHub': 'https://github.com/{}',
            'Reddit': 'https://reddit.com/u/{}',
            'Snapchat': 'https://www.snapchat.com/add/{}',
        }
        
        print(f'\n{yel}[*] Searching for @{self.username} across platforms...{wit}\n')
        self.search_all()
    
    def search_all(self):
        """Search username on all platforms"""
        found = []
        
        for platform, url_template in self.platforms.items():
            try:
                url = url_template.format(self.username)
                response = get(url, headers={'User-Agent': get_user_agent()}, timeout=5)
                
                if response.status_code == 200:
                    print(f'{grn}[+]{wit} Found on {platform}: {url}')
                    found.append(platform)
                else:
                    print(f'{red}[-]{wit} Not found on {platform}')
            except Exception as e:
                print(f'{yel}[!]{wit} Error checking {platform}: {str(e)[:30]}...')
        
        print(f'\n{grn}[+] Summary: Found on {len(found)} platforms{wit}')
        go_back()

class EmailSearcher:
    """Email information search across services"""
    
    def __init__(self):
        self.email = input(f'{yel}[+]{wit} Enter Email: ').strip()
        
        if '@' not in self.email:
            print(f'{red}[-] Invalid email format{wit}')
            go_back()
            return
        
        self.domain = self.email.split('@')[1]
        print(f'\n{yel}[*] Searching for {self.email}...{wit}\n')
        self.search_services()
    
    def search_services(self):
        """Search email across services"""
        services = {
            'Microsoft': 'https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress={}',
            'Instagram': 'https://www.instagram.com/accounts/account_recovery_send_ajax/',
            'Twitter': 'https://twitter.com/users/email_available?email={}',
        }
        
        found_on = []
        
        # Microsoft check
        try:
            response = get(services['Microsoft'].format(self.email), timeout=10)
            if 'MSAccount' in response.text:
                print(f'{grn}[+]{wit} Email linked to Microsoft Account')
                found_on.append('Microsoft')
        except:
            pass
        
        # Instagram check
        try:
            response = post(
                services['Instagram'],
                headers={'User-Agent': get_user_agent()},
                data={'email': self.email},
                timeout=10
            )
            if 'ok' in response.text.lower():
                print(f'{grn}[+]{wit} Email linked to Instagram')
                found_on.append('Instagram')
        except:
            pass
        
        # Twitter check
        try:
            response = get(services['Twitter'].format(self.email), timeout=10)
            if '"taken":true' in response.text:
                print(f'{grn}[+]{wit} Email linked to Twitter')
                found_on.append('Twitter')
        except:
            pass
        
        print(f'\n{grn}[+] Summary: Found on {len(found_on)} services{wit}')
        go_back()

def ip_info_lookup():
    """Lookup IP address information"""
    ips = input(f'\n{yel}[$]{wit} Enter IP address: ').strip()
    
    if not ips:
        print(f'{red}[-] Empty IP address{wit}')
        go_back()
        return
    
    try:
        response = get(f'https://get.geojs.io/v1/ip/geo/{ips}.json', timeout=10)
        data = response.json()
        
        print(f'\n{grn}[+] IP Information:{wit}')
        print(f'{grn}{'━' * 50}{wit}')
        print(f'{grn}[+]{wit} IP Address: {ips}')
        print(f'{grn}[+]{wit} Country: {data.get("country", "N/A")}')
        print(f'{grn}[+]{wit} City: {data.get("city", "N/A")}')
        print(f'{grn}[+]{wit} Timezone: {data.get("timezone", "N/A")}')
        print(f'{grn}[+]{wit} ISP: {data.get("organization", "N/A")}')
        print(f'{grn}[+]{wit} Latitude: {data.get("latitude", "N/A")}')
        print(f'{grn}[+]{wit} Longitude: {data.get("longitude", "N/A")}')
        print(f'{grn}{'━' * 50}{wit}\n')
    except json.decoder.JSONDecodeError:
        print(f'{red}[-] Invalid IP address{wit}')
    except Exception as e:
        print(f'{red}[-] Error: {str(e)}{wit}')
    finally:
        go_back()

def print_banner(platform_type):
    """Print application banner"""
    if platform_type in LINX:
        banner = f"""{grn}
╔═══════════════════════════════════════════════════╗
║                   ORECA v2.0                      ║
║          Advanced OSINT Information Tool          ║
║                                                   ║
║            Made by @blackevil518                 ║
║          Website: https://t.me/blackevil518      ║
╚═══════════════════════════════════════════════════╝
{wit}"""
    else:
        banner = f"""{bloFT}
╔═══════════════════════════════════════════════════╗
║                   ORECA v2.0                      ║
║        Mobile OSINT Information Gathering         ║
║                                                   ║
║            Made by @blackevil518                 ║
║          Website: https://t.me/blackevil518      ║
╚═══════════════════════════════════════════════════╝
{wit}"""
    
    print(banner)

def settings():
    """Main settings menu"""
    global PLATFORM_TYPE
    
    if PLATFORM_TYPE in LINX:
        menu = f"""
{bloFT}{'━' * 50}{wit}
{grn}MAIN MENU{wit}
{bloFT}{'━' * 50}{wit}

{yel}1. User Information Collection{wit}
{yel}2. Website Information Gathering{wit}
{yel}3. Exit{wit}

{yel}[$]{wit} Enter your choice: """
        
        choice = input(menu).strip()
        
        if choice == '1':
            user_menu()
        elif choice == '2':
            website_menu()
        elif choice == '3':
            print(f'{red}[*] Exiting...{wit}')
            sys.exit(0)
        else:
            print(f'{red}[-] Invalid choice{wit}')
            settings()
    else:
        menu = f"""
{bloFT}{'━' * 50}{wit}
{grn}MOBILE MENU{wit}
{bloFT}{'━' * 50}{wit}

{yel}1. Search Phone Number{wit}
{yel}2. Search Username{wit}
{yel}3. Search Email{wit}
{yel}4. Exit{wit}

{yel}[$]{wit} Enter your choice: """
        
        choice = input(menu).strip()
        
        if choice == '1':
            PhoneSearcher()
        elif choice == '2':
            UsernameSearcher()
        elif choice == '3':
            EmailSearcher()
        elif choice == '4':
            print(f'{red}[*] Exiting...{wit}')
            sys.exit(0)
        else:
            print(f'{red}[-] Invalid choice{wit}')
            settings()

def user_menu():
    """User information gathering menu"""
    menu = f"""
{bloFT}{'━' * 50}{wit}
{grn}USER INFORMATION TOOLS{wit}
{bloFT}{'━' * 50}{wit}

{yel}1. Search Email on Websites{wit}
{yel}2. Phone Number Lookup{wit}
{yel}3. Username Search{wit}
{yel}4. IP Address Information{wit}
{yel}5. Back to Menu{wit}

{yel}[$]{wit} Enter your choice: """
    
    choice = input(menu).strip()
    
    if choice == '1':
        EmailSearcher()
    elif choice == '2':
        PhoneSearcher()
    elif choice == '3':
        UsernameSearcher()
    elif choice == '4':
        ip_info_lookup()
    elif choice == '5':
        settings()
    else:
        print(f'{red}[-] Invalid choice{wit}')
        user_menu()

def website_menu():
    """Website information gathering menu"""
    menu = f"""
{bloFT}{'━' * 50}{wit}
{grn}WEBSITE INFORMATION TOOLS{wit}
{bloFT}{'━' * 50}{wit}

{yel}1. Basic Website Information{wit}
{yel}2. Extract Subdomains{wit}
{yel}3. Extract Links{wit}
{yel}4. Port Scanner{wit}
{yel}5. Back to Menu{wit}

{yel}[$]{wit} Enter your choice: """
    
    choice = input(menu).strip()
    
    if choice in ['1', '2', '3', '4']:
        WebScanner(choice)
    elif choice == '5':
        settings()
    else:
        print(f'{red}[-] Invalid choice{wit}')
        website_menu()

def main():
    """Main entry point"""
    global PLATFORM_TYPE
    
    try:
        platform_menu = f"""{red}
{'='*50}
Select your platform:
{'='*50}

{yel}1/k) Kali Linux / Windows / Mac{wit}
{yel}2/p) iPhone / Android / Mobile{wit}

{yel}[$]{wit} Enter: {wit}"""
        
        PLATFORM_TYPE = input(platform_menu).strip().lower()
        
        if PLATFORM_TYPE not in ['1', 'k', '2', 'p']:
            print(f'{red}[-] Invalid platform selection{wit}')
            sys.exit(1)
        
        print(f'\n{grn}[+] Initializing...{wit}\n')
        sleep(0.5)
        
        print_banner(PLATFORM_TYPE)
        settings()
    except KeyboardInterrupt:
        print(f'\n{red}[!] Interrupted by user{wit}')
        sys.exit(0)
    except Exception as e:
        print(f'{red}[-] Error: {str(e)}{wit}')
        sys.exit(1)

if __name__ == '__main__':
    main()
