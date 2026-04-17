import requests
from django.conf import settings

def send_message(phone,message):

    url="https://graph.facebook.com/v18.0/YOUR_ID/messages"

    headers={
        "Authorization":f"Bearer {settings.WHATSAPP_TOKEN}",
        "Content-Type":"application/json"
    }

    data={
        "messaging_product":"whatsapp",
        "to":phone,
        "type":"text",
        "text":{"body":message}
    }

    requests.post(url,json=data,headers=headers)
