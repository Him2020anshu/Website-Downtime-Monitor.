# 🌐 Website Downtime Monitor

A lightweight Python-based tool that continuously monitors websites or services and **alerts you instantly when downtime is detected**.
It leverages the UptimeRobot API for status checks and Gmail SMTP for sending notifications.

---

## 🚀 Features

* Monitor multiple websites/services
* Detect downtime in real-time
* Send instant email alerts
* Easy configuration
* Adjustable monitoring interval (default: 60 seconds)
* Customizable alert messages

---

## 📌 How It Works

1. The script queries the UptimeRobot API
2. Checks the status of configured websites
3. If any website is **DOWN**, an email alert is triggered
4. The process repeats at a fixed interval

---

## 🧰 Tech Stack

* Python 3
* requests library
* SMTP (Gmail)
* UptimeRobot API

---

## 📋 Prerequisites

* Python 3.6 or higher
* Internet connection
* Gmail account (for alerts)
* UptimeRobot account (API key required)

---

## ⚙️ Setup Guide

### 1. Clone Repository

git clone https://github.com/Manu-Abuya/Website-Uptime-Monitor.git
cd Website-Uptime-Monitor

### 2. Install Dependencies

pip install requests

### 3. Get UptimeRobot API Key

* Create account at https://uptimerobot.com/
* Go to My Settings → API Settings
* Copy your Main API Key

### 4. Configure Gmail SMTP

* Enable App Password (recommended)
* Avoid using your real password

### 5. Configure Script

Open `website_monitor.py` and update:

API_KEY = "YOUR_UPTIMEROBOT_API_KEY"
EMAIL = "[your_email@gmail.com](mailto:your_email@gmail.com)"
PASSWORD = "your_app_password"
TO_EMAIL = "[recipient_email@gmail.com](mailto:recipient_email@gmail.com)"

### 6. Run the Script

python website_monitor.py

---

## 🛠 Customization

* Add more websites in the `websites` list
* Change monitoring interval using time.sleep(seconds)
* Customize email message format in send_email()
* Add logging for downtime history

---

## 📊 Example Alert

Subject: Website Down Alert

Your monitored website is DOWN.

Website: Example.com
Status: DOWN
Time: 12:45 PM

Please take immediate action.

---

## 📌 Use Cases

* Monitor personal projects
* Track production servers
* Get alerts during outages
* Useful for DevOps and backend monitoring

---

## ⚠️ Security Note

* Do not expose API keys or credentials publicly
* Use environment variables for security
* Prefer App Password instead of real Gmail password

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

* UptimeRobot API for uptime monitoring
* Gmail SMTP for email notifications

---


