import requests
import os

EMAILREP_API = os.getenv("EMAILREP_API", "https://emailrep.io")
NUMVERIFY_API_KEY = os.getenv("NUMVERIFY_API_KEY")
IPINFO_API_KEY = os.getenv("IPINFO_API_KEY")

def lookup_email(email):
    try:
        resp = requests.get(f"{EMAILREP_API}/{email}")
        if resp.status_code == 200:
            data = resp.json()
            return f"[EmailRep] Reputation: {data.get('reputation')}, Suspicious: {data.get('suspicious')}, Blacklisted: {data.get('details', {}).get('blacklisted')}"
        return "EmailRep: No data or rate limit exceeded."
    except Exception as e:
        return f"EmailRep Error: {e}"

def lookup_ip(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        if IPINFO_API_KEY:
            url += f"?token={IPINFO_API_KEY}"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            return f"[IPInfo] IP: {ip}\nCountry: {data.get('country')}\nCity: {data.get('city')}\nOrg: {data.get('org')}"
        return "IPInfo: No data found."
    except Exception as e:
        return f"IPInfo Error: {e}"

def lookup_phone(phone):
    try:
        if not NUMVERIFY_API_KEY:
            return "Numverify API key not set"
        url = f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={phone}&format=1"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            return f"[Numverify] Valid: {data.get('valid')}\nCountry: {data.get('country_name')}\nCarrier: {data.get('carrier')}\nLocation: {data.get('location')}"
        return "Numverify: No data found."
    except Exception as e:
        return f"Numverify Error: {e}"

def lookup_username(username):
    return f"Manual search:\nhttps://github.com/{username}\nhttps://namecheckup.com/user/{username}\nhttps://t.me/{username}"

def lookup_domain(domain):
    try:
        resp = requests.get(f'https://api.hackertarget.com/whois/?q={domain}')
        if resp.status_code == 200:
            return "[WHOIS]\n" + resp.text[:1000]
        return "WHOIS: No data found."
    except Exception as e:
        return f"WHOIS Error: {e}"

def lookup_telegram_id(user_id):
    return f"Telegram ID: {user_id}"

def lookup_darknet(keyword):
    return f"Simulated darknet search for: {keyword}"

def generate_report(query):
    return (
        f"Report for {query}\n"
        f"{lookup_email(query)}\n"
        f"{lookup_ip(query)}\n"
        f"{lookup_domain(query)}\n"
        f"{lookup_username(query)}"
    )
