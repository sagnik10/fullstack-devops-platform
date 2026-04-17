import requests
from django.conf import settings

def create_zoom_meeting(topic):

    url="https://api.zoom.us/v2/users/me/meetings"

    headers={
        "Authorization":f"Bearer {settings.ZOOM_TOKEN}"
    }

    payload={
        "topic":topic,
        "type":2,
        "settings":{
            "auto_recording":"cloud"
        }
    }

    r=requests.post(url,json=payload,headers=headers)

    return r.json()
