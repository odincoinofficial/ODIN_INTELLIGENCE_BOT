import requests

def lookup_email(email):
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
    return f"Username lookup for: {username} (stub)"

def lookup_domain(domain):
    try:
        resp = requests.get(f'https://api.hackertarget.com/whois/?q={domain}')
        if resp.status_code == 200:
            return resp.text[:1000]
        return "No WHOIS data found."
    except Exception as e:
        return f"Error: {e}"

def lookup_phone(phone):
    return f"Phone lookup for: {phone} (stub or API integration)"

def lookup_telegram_id(user_id):
    return f"Telegram ID: {user_id} — public lookup not available via Bot API"

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
