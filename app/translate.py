import json
import requests
from flask_babel import _
from app import app


def translate(text, source_language, dest_language):
    if 'YA_KEY' not in app.config or \
            not app.config['YA_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': app.config['YA_KEY']}
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json'
                     '/translate?key={}&text={}&lang={}-{}'.format(
                         app.config['YA_KEY'], text, source_language, dest_language), headers=auth)
   # print(r.content[0])
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    
    return json.loads(r.content)['text'][0]