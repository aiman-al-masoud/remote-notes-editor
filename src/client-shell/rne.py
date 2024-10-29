#!/bin/python3

import sys
import requests as req
import os
from time import sleep
import json

PATH_SETTINGS='settings.json'

match sys.argv[1:]:

    case ['open-file', path]:

        settings = json.loads(open(PATH_SETTINGS).read())
        BASE = settings['BASE']

        r = req.post(os.path.join(BASE, 'set-filepath'), json={'filepath': path})
        print(r.text)

        text = open(path).read()
        req.post(os.path.join(BASE, 'set-text'), json={'text': text})
        print(r.text)

        while True:

            text_new = req.post(os.path.join(BASE, 'get-text')).text

            if text != text_new:

                with open(path, 'w') as f:
                    f.write(text_new)

            sleep(1)
    
    case ['set-base-url', url]:

        if os.path.exists(PATH_SETTINGS):
            settings = json.loads(open(PATH_SETTINGS).read())
        else:
            settings = {}

        with open(PATH_SETTINGS, 'w+') as f:
            f.write(json.dumps({**settings, 'BASE': url}))
