import urllib3
import os
import json
from datetime import datetime

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
"""

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

def GetLongLivedAccessToken(fb_url,secrets):
    response = GetAccessToken(fb_url=fb_url,config=secrets)
    if response:
        long_lived_access_token = response['access_token']
        return long_lived_access_token

def BackupSecrets(fname):
    now = datetime.today().isoformat()
    backup = f'{fname}.{now}'
    os.rename(fname,backup)

def WriteSecrets(fname,config):
    with open(fname,'w') as fw:
        fw.write(json.dumps(config, indent=2))

def ReadSecrets(fname):
    with open(fname,'r') as fr:
        json_data = json.load(fr)
        return json_data

def main(fname):
    fb_url = "https://graph.facebook.com"
    print(Usage)
    short_lived_access_token = input('Short Lived Token: ')
    if os.path.exists(fname):
        secrets = ReadSecrets(fname=fname)
        if secrets:
            secrets['short_lived_access_token'] = short_lived_access_token
            long_lived_access_token = GetLongLivedAccessToken(fb_url=fb_url,secrets=secrets)
            if long_lived_access_token:
                secrets['long_lived_access_token'] = long_lived_access_token
                BackupSecrets(fname)
                WriteSecrets(fname=fname, config=secrets)

if __name__ == "__main__":
    facebook_secrets = os.environ['FACEBOOK_CONFIG']
    if facebook_secrets:
        main(facebook_secrets)
    else:
        print('FACEBOOK_CONFIG not set as an env variable')