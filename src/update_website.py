import os
import json
from datetime import datetime
from glob import glob

md_template = """
---
Date:   #DATE#
Topic:  #TOPIC#
Content: #CONTENT#
---
#BODY#

We are open to new members and if you're interested please come along to 
Curborough Community Centre Code Club at 5:30pm each Wednesday. 
Bring a laptop with wifi capability if you can
Look forward to meeting you :-)

Find us:
[Code Club Website](https://lichfield-code-club.github.io/)
[Facebook]
[Discord]
"""

def ReadJson(fname):
    with open(fname,'r') as fr:
        json_data = json.load(fr)
        return json_data

def CreateWebPost(fname):
    posts = ReadJson(fname=fname)
    for post in posts['data']:
        md_date = post['created_time'].split('+')[0].replace('T','-')
        meeting_date = post['created_time'].split('T')[0]

        web_post = md_template
        web_post = web_post.replace('#TOPIC#','Club Meeting')
        web_post = web_post.replace('#DATE#',meeting_date)
        web_post = web_post.replace('#CONTENT#','Summary')
        web_post = web_post.replace('#BODY#',post['message'])

        md_file = f'_posts/{meeting_date}-Meeting.md'
        with open(md_file,'w') as fw:
            fw.write(web_post)

def UpdateWebsite(fname):
    config = ReadJson(fname)
    if config:
        filelist = glob('resources/facebook_posts1.json')
        for file in filelist:
            CreateWebPost(fname=file)
    else:
        print('GetFacebookPosts Response','Failed')


if __name__ == "__main__":
    facebook_config = os.environ['FACEBOOK_CONFIG']
    if facebook_config:
        UpdateWebsite(fname=facebook_config)
    else:
        print('FACEBOOK_CONFIG not set as an env variable') 
