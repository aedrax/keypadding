#!/usr/bin/env python3
import json
import requests
import time

words = set()

for letter in "abcdefghijklmnopqrstuvwxyz":
    page = 1
    while True:
        url = f"https://www.dictionary.com/e/crb-ajax/cached.php?wordLength=6&letter={letter}&action=get_wf_widget_page&page={page}"
        r = requests.get(url)
        content = r.json()
        if content["success"] is False:
            break
        words.update(content["data"]["words"])
        page = page + 1
        time.sleep(1)

with open("words.json", "w") as word_file:
    json.dump({"words": list(words)}, word_file)
