import json
import re
from konlpy.tag import Twitter
from collections import Counter

def json_to_str(filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')
    json_string = jsonfile.read()
    json_data = json.loads(json_string)

    data = ''
    for item in json_data:
        # print(item)
        value = item.get(key)
        if value is None:
            continue

        data += re.sub(r'[^\w]', '', value)


    return data


def count_word_freq(data):
    # data를 단어로 나누기
    twitter = Twitter()
    nouns = twitter.nouns(data)

    # 단어당 갯수 뽑기
    count = Counter(nouns)
    return count
