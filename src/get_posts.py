import urllib3
import json
import os
from datetime import datetime, timezone

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

def SaveJson(fname, data):
    # Add 'retrieved_time' to each item in the list
    for item in data:
        item['retrieved_time'] = datetime.now(timezone.utc).isoformat()
    with open(fname, 'w') as fw:
        fw.write(json.dumps(data, indent=2))
        print('JSON Written to File', fname)

def ReadSecrets(fname):
    with open(fname, 'r') as fr:
        json_data = json.load(fr)
        return json_data

def FacebookRequest(url):
    with urllib3.PoolManager() as http:
        r = http.request('GET', url)
        if r.status == 200:
            return json.loads(r.data.decode('utf-8'))

def GetPageToken(config):
    if config:
        fb_url = config['fb_url']
        page_id = config['page_id']
        access_token = f"access_token={config['long_lived_access_token']}"
        fields = "fields=access_token"

        fb_request  = f"{fb_url}/{page_id}"
        fb_request += f"?{fields}"
        fb_request += f"&{access_token}"

        response = FacebookRequest(fb_request)
        if response and isinstance(response, dict) and 'access_token' in response:
            return response
        print('GetPageToken failed or unexpected response:', response)
        return None

def GetPosts(config):
    response = GetPageToken(config=config)
    if response:
        page_access_token = response['access_token']
        page_id = config['page_id']
        fb_url = config['fb_url']
        fb_api_version = 'v24.0'

        fb_request = f'{fb_url}/{fb_api_version}/{page_id}/feed'
        fb_request += '?fields=attachments,created_time,updated_time,id,message,permalink_url'
        fb_request += f'&access_token={page_access_token}'

        next = True
        pageno = 0
        while next:
            response = FacebookRequest(fb_request)
            if response:
                pageno += 1
                if 'data' in response.keys():
                    json_file = config['facebook_posts'].replace('*.json', f'{pageno}.json')
                    json_data = response['data']
                    SaveJson(fname=json_file, data=json_data)
                next = 'paging' in response.keys() and 'next' in response['paging']
                if next:
                    fb_request = response['paging']['next']

def GetFacebookPosts(fname):
    config = ReadSecrets(fname)
    if config:
        GetPosts(config)
    else:
        print(f'failed to read config file: {fname}')


if __name__ == "__main__":
    config = 'src/config/facebook.json'
    if os.path.exists(config):
        GetFacebookPosts(fname=config)
    else:
        print(f'FACEBOOK CONFIG not found: {config}')
