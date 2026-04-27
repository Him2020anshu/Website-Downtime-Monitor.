import requests
import time
import smtplib
from email.mime.text import MIMEText

# ---------------- CONFIG ----------------
WEBSITES = [
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com"  # add your sites
]

CHECK_INTERVAL = 60  # seconds

EMAIL = "rajh92361@gmail.com"
PASSWORD = "password"
TO_EMAIL = "jhasunny@gmail.com"
# ----------------------------------------


def send_email(site):
    subject = "🚨 Website Down Alert"
    body = f"Website {site} is DOWN. Please check immediately!"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = TO_EMAIL

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, TO_EMAIL, msg.as_string())
        print(f"[EMAIL SENT] Alert for {site}")
    except Exception as e:
        print("Email failed:", e)


def check_website(site):
    try:
        response = requests.get(site, timeout=5)
        if response.status_code == 200:
            print(f"[UP] {site}")
            return True
        else:
            print(f"[DOWN] {site} - Status: {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print(f"[DOWN] {site} - No response")
        return False


def monitor():
    while True:
        for site in WEBSITES:
            if not check_website(site):
                send_email(site)
        print("----- Checking again in", CHECK_INTERVAL, "seconds -----")
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    monitor()