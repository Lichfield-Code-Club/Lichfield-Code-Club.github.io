import urllib3
import os
import json

"""
# Page/Feed url: https://developers.facebook.com/docs/graph-api/reference/page/
"""

def ReadSecrets(fname):
    with open(fname,'r') as fr:
        json_data = json.load(fr)
        return json_data['access_token'], json_data['page_id']

def GetPosts():
    fb_url = "https://graph.facebook.com"
    secrets_file = '.secrets'
    fields = ['posts','photos','picture']
    fields = '%2C'.join(fields)

    access_token, page_id = ReadSecrets(secrets_file)

    fb_page_url = f'{fb_url}/{page_id}?access_token={access_token}&fields={fields}'
    print(fb_page_url)
    http = urllib3.PoolManager()
    r = http.request('GET', fb_page_url)
    if r.status == 200:
        return r.data

def GetFacebookPosts(fname):
    facebook_posts = GetPosts()
    if facebook_posts:
        decoded = facebook_posts.decode('ascii')
        json_data = json.loads(decoded)
        with open(fname,'w') as fw:
            fw.write(json.dumps(json_data, indent=2))

def ReadPosts(fname):
    with open(fname,'r') as fr:
        json_data = json.load(fr)
        return json_data

def CreateWebPost(post_data):
    for post_num, post_message in enumerate(post_data['posts']['data']):
        print(post_num,post_message)

if __name__ == "__main__":
    facebook_posts_filename = "facebook_posts.json"
    if not os.path.exists(facebook_posts_filename):
        post_data = GetFacebookPosts(facebook_posts_filename)
    if os.path.exists(facebook_posts_filename):
        post_data = ReadPosts(facebook_posts_filename)
        CreateWebPost(post_data)