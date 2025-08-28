# 🌐 Social Media & Communication Automation with Python

## 📌 Overview
This project provides Python scripts to automate posting and communication tasks across multiple platforms:

- 📱 Send SMS messages  
- 📞 Make phone calls  
- 💬 Send WhatsApp messages  
- 💼 Post on LinkedIn  
- 🐦 Post on Twitter (X)  
- 📘 Post on Facebook  
- 📸 Post on Instagram  

It leverages official APIs (Twilio, LinkedIn API, Twitter API, Facebook Graph API, Instagram Graph API).

---

## ⚙️ Requirements
- Python 3.8+  
- API credentials for respective services  
- A `.env` file to store secrets securely  

Install dependencies:
```bash
pip install requests tweepy python-dotenv twilio
```

social-media-automation/
│── sms_send.py            # Send SMS using Twilio
│── phone_call.py          # Make phone calls using Twilio
│── whatsapp_send.py       # Send WhatsApp messages using Twilio
│── linkedin_post.py       # Post on LinkedIn
│── twitter_post.py        # Post on Twitter (X)
│── facebook_post.py       # Post on Facebook
│── instagram_post.py      # Post on Instagram
│── .env                   # API keys and secrets
│── README.md              # Documentation

# Twilio (SMS, Phone, WhatsApp)
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE=+1234567890
TO_PHONE=+0987654321

# LinkedIn
LINKEDIN_ACCESS_TOKEN=your_linkedin_access_token

# Twitter (X)
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_SECRET=your_access_secret

# Facebook
FB_PAGE_ID=your_page_id
FB_ACCESS_TOKEN=your_fb_page_access_token

# Instagram
IG_ACCESS_TOKEN=your_instagram_access_token
IG_ACCOUNT_ID=your_instagram_business_account_id

# Send WhatsApp Message
python whatsapp_send.py
