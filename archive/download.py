import datetime
from urllib.parse import urlencode

import vlermv, requests

GROUP_ID = 1463661227181475
URL = 'https://graph.facebook.com/v2.2/%s/feed % GROUP_ID'
CACHE = os.path.join('~', '.immaterial-digital-labor', 'archive')

def url(access_token):
    return URL + '?' + urlencode({
        'access_token': access_token,
        'format': 'json',
        'method': 'get',
        'pretty': '0',
        'suppress_http_code': '1',
    })

get = vlermv.cache(os.path.join(CACHE, datetime.date.today()))(requests.get)

def download(access_token):
    '''
    Return an iterable of "data" entries, each containing the following keys.

    * likes
    * to
    * created_time
    * actions
    * message
    * updated_time
    * comments
    * privacy
    * id
    * from
    * type
    '''

    response = get(url(access_token))
    while response.ok:
        payload = response.json()
        yield from payload['data']
        if 'paging' in payload:
            response = get(payload['paging']['next'])
        else:
            break
