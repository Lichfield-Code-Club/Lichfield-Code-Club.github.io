import urllib3
import os
import json

Usage = """
https://developers.facebook.com/docs/pages/access-tokens/
Get A Short Lived Access Token
    The Graph Explorer tool
        https://developers.facebook.com/docs/graph-api/guides/explorer#get-token-dropdown
        https://developers.facebook.com/tools/explorer/
            Select App from dropdown e.g. webupdate
            Select Token Type e.g. Page Token
            Select Page Name e.g. Curborough Community Centre Code Club
            Generate Access Token: 
    The Facebook Login Dialog       
"""

def SaveJson(fname,data):
    with open(fname,'w') as fw:
        fw.write(json.dumps(data, indent=2))
        print('JSON Written to File',fname)

def ReadSecrets(fname):
    with open(fname,'r') as fr:
        json_data = json.load(fr)
        return json_data

def FacebookRequest(url):
    with urllib3.PoolManager() as http:
        r = http.request('GET', url)
        if r.status == 200:
            return json.loads(r.data.decode('utf-8'))
        print('FacebookRequest',r.status,r.reason)
        print('Request',url)
        print('Response',r.data)

def GetAccessToken(fb_url,config):
    if config:
        grant_type = 'grant_type=fb_exchange_token'
        client_id = f"client_id={config['app_id']}"
        client_secret = f"client_secret={config['app_secret']}"
        fb_exchange_token = f"fb_exchange_token={config['short_lived_access_token']}"

        fb_request  = f"{fb_url}/oauth/access_token"
        fb_request += f"?{grant_type}"
        fb_request += f"&{client_id}"
        fb_request += f"&{client_secret}"
        fb_request += f"&{fb_exchange_token}"

        response = FacebookRequest(fb_request)
        if response: 
            return response
        print('GetAccessToken','Failed')

def GetPageToken(config):
    if config:
        fb_url = config['fb_url']
        page_id=config['page_id']
        access_token=f"access_token={config['long_lived_access_token']}"
        fields = "fields=access_token"

        fb_request  = f"{fb_url}/{page_id}"
        fb_request += f"?{fields}"
        fb_request += f"&{access_token}"

        response = FacebookRequest(fb_request)
        if response: 
            return response
        print('GetPageToken','Failed')

def GetPosts(config):
    response = GetPageToken(config=config)
    if response:
        fields = ['posts','photos','picture']
        fields = '%2C'.join(fields)
        page_access_token = response['access_token']
        page_id= config['page_id']
        fb_url = config['fb_url']

        fb_request = f'{fb_url}/{page_id}'
        fb_request += f'?access_token={page_access_token}'
        fb_request += f'&fields={fields}'

        response = FacebookRequest(fb_request)
        if response: 
            print('Paging',response['posts']['paging']['next'])
            return response
        else: 
            print('GetPosts Response','Failed')
    else:
        print('GetPageToken','Failed')

def GetFacebookPosts(fname):
    config = ReadSecrets(fname)
    if config:
        facebook_posts = GetPosts(config)
        if facebook_posts:
            json_filename = config['facebook_posts']
            SaveJson(fname=json_filename,data=facebook_posts)
        else:
            print('GetFacebookPosts Response','Failed')


if __name__ == "__main__":
    secrets_file = 'src/.secrets'
    GetFacebookPosts(fname=secrets_file)
