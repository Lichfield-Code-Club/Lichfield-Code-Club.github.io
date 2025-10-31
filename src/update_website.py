import os
import json
from datetime import datetime
from glob import glob

md_template = """---
layout: post
title: "Club Meeting: #DATE#"
date: #DATE#
Topic: "#TOPIC#"
categories: [Code Club]
tags: [Coding, Kids, Education, Community]
---
#BODY#

#CONTENT#

* [Facebook Post](#PERMALINK#)

## 📍 Location

Curborough Community Centre  
WS13 7NY  
Code Club  
Wednesdays 5:30 - 6:30 PM  
7 - 15 year olds welcome  

---
"""

def ReadJson(fname):
    with open(fname,'r') as fr:
        json_data = json.load(fr)
        return json_data

def HandleAttachments(post_data):
    retval = ''
    if 'attachments' in post_data.keys():
        attachments = post_data['attachments']
        if 'data' in attachments.keys():
            data = attachments['data']
            for data_item in data:
                if 'title' in data_item.keys() and 'url' in data_item.keys():
                    retval += f"[{data_item['title']}]({data_item['url']})"

                if 'media' in data_item.keys():
                    media = data_item['media']
                    if 'image' in media.keys():
                        image = media['image']
                        retval += f"![ALT TEXT]({image['src']})"
    return retval

def CreateWebPost(fname):
    posts = ReadJson(fname=fname)
    more = True
    for post in posts:
        if not 'created_time' in post.keys():
            print('File has posts with no created_time',fname)
        else:
            if more:
                content = HandleAttachments(post_data=post)

                md_date = post['created_time'].split('+')[0].replace('T','-')
                md_day  = post['created_time'].split('T')[0]
                md_file = f'_posts/{md_day}-Meeting.md'
                web_post = md_template
                web_post = web_post.replace('#DATE#',md_day)
                # web_post = web_post.replace('#IMAGE#',content)
                web_post = web_post.replace('#PERMALINK#',post['permalink_url'])
                web_post = web_post.replace('#TOPIC#','Club Meeting')
                web_post = web_post.replace('#CONTENT#',content)
                if 'message' in post.keys():
                    web_post = web_post.replace('#BODY#',post['message'])
                    tag_line = ' '.join(post['message'].split(' ')[0:4])
                    # if not 'http' in tag_line:
                    #     md_file = f'_posts/{meeting_date}-{tag_line}.md'
                else:
                    web_post = web_post.replace('#BODY#','')
                if os.path.exists(md_file):
                    os.remove(md_file)
                with open(md_file,'w') as fw:
                    fw.write(web_post)
                if os.path.exists(md_file):
                    print('Web Post Created',md_file)
                # more = False

def UpdateWebsite(fname):
    config = ReadJson(fname)
    if config:
        filelist = glob(config['facebook_posts'])
        if not filelist:
            print('No Facebook Post files found', config['facebook_posts'])
            return
        filelist.sort(key=lambda x: int(os.path.basename(x).replace('facebook_posts', '').replace('.json', '')))
        for file in filelist:
            CreateWebPost(fname=file)
    else:
        print('GetFacebookPosts Response','Failed')


if __name__ == "__main__":
    facebook_config = 'src/config/facebook.json'
    if os.path.exists(facebook_config):
        UpdateWebsite(fname=facebook_config)
    else:
        print(f'FACEBOOK_CONFIG file not found', facebook_config) 
