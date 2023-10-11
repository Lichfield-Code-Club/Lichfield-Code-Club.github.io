import os
import json
from datetime import datetime
from glob import glob

md_template = """---
Date:   #DATE#
Topic:  #TOPIC#
Content: #CONTENT#
---
#BODY#

# [Facebook Link](#PERMALINK#)

#
Curborough Community Centre
WS13 7NY
Code Club
Wednesdays 5:30 - 6:30pm
7 - 15 year olds welcome

Club Links:
[Code Club Website](https://lichfield-code-club.github.io/)

[Facebook Page](https://www.facebook.com/LichfieldCoders)

[Discord club messages](https://discord.gg/szz6xGK)
"""

def ReadJson(fname):
    with open(fname,'r') as fr:
        json_data = json.load(fr)
        return json_data

def CreateWebPost(fname):
    posts = ReadJson(fname=fname)
    for post in posts:
        if not 'created_time' in post.keys():
            print('File has posts with no created_time',fname)
        else:
            md_date = post['created_time'].split('+')[0].replace('T','-')
            meeting_date = post['created_time'].split('T')[0]
            md_file = f'_posts/{meeting_date}-Meeting.md'

            web_post = md_template
            web_post = web_post.replace('#PERMALINK#',post['permalink_url'])
            web_post = web_post.replace('#TOPIC#','Club Meeting')
            web_post = web_post.replace('#DATE#',meeting_date)
            web_post = web_post.replace('#CONTENT#','Summary')
            if 'message' in post.keys():
                web_post = web_post.replace('#BODY#',post['message'])
                tag_line = '_'.join(post['message'].split(' ')[0:4])
                if not 'http' in tag_line:
                    md_file = f'_posts/{meeting_date}-{tag_line}.md'
            else:
                web_post = web_post.replace('#BODY#','')
            if os.path.exists(md_file):
                os.remove(md_file)
            with open(md_file,'w') as fw:
                fw.write(web_post)

def UpdateWebsite(fname):
    config = ReadJson(fname)
    if config:
        filelist = glob('resources/facebook_posts*.json')
        filelist.sort()
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
