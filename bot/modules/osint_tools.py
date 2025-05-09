
import requests

def lookup_email(email):
    # Пример: use hunter.io или EmailRep.io
    try:
        resp = requests.get(f'https://emailrep.io/{email}')
        if resp.status_code == 200:
            data = resp.json()
            return f"Reputation: {data.get('reputation')}, Suspicious: {data.get('suspicious')}"
        return "No data found or rate-limited."
    except Exception as e:
        return f"Error: {e}"

def lookup_ip(ip):
    try:
        resp = requests.get(f'https://ipinfo.io/{ip}/json')
        if resp.status_code == 200:
            data = resp.json()
            return f"IP: {ip}\nCountry: {data.get('country')}\nCity: {data.get('city')}\nOrg: {data.get('org')}"
        return "No data found."
    except Exception as e:
        return f"Error: {e}"

def lookup_username(username):
    return f"Check manually: https://www.google.com/search?q={username}+site:twitter.com or GitHub, Telegram, etc."

def lookup_domain(domain):
    try:
        resp = requests.get(f'https://api.hackertarget.com/whois/?q={domain}')
        if resp.status_code == 200:
            return resp.text[:1000]  # Ограничим вывод
        return "No WHOIS data found."
    except Exception as e:
        return f"Error: {e}"



def lookup_phone(phone):
    try:
        api_key = "your_numverify_api_key"
        url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone}&format=1"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            return f"Phone: {phone}\nCountry: {data.get('country_name')}\nLocation: {data.get('location')}\nCarrier: {data.get('carrier')}"
        return "No data or invalid API key."
    except Exception as e:
        return f"Error: {e}"



def lookup_telegram_id(user_id):
    return f"Telegram ID: {user_id} — no extra public data via Bot API."

def lookup_social(username):
    return f"Suggested search:\\nhttps://github.com/{username}\\nhttps://namecheckup.com/user/{username}\\nhttps://t.me/{username}"

def lookup_darknet(keyword):
    return f"Simulated darknet lookup for: {keyword}. Full darknet scanning requires proxy and TOR network."

def generate_report(query):
    return (
        f"Full OSINT Report for: {query}\n"
        f"Email: {lookup_email(query)}\n"
        f"IP: {lookup_ip(query)}\n"
        f"Domain: {lookup_domain(query)}\n"
        f"User: {lookup_username(query)}"
    )
