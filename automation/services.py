import openai
from django.conf import settings

def generate_article(topic):

    prompt=f"Write devops tutorial about {topic}"

    res=openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content
