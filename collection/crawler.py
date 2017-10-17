# crawler.py
import os

from .api import api
from datetime import datetime, timedelta
import json


RESULT_DIRECTORY = '__results__/crawling'


# 전처리 -> 데이터 정규화
def pre_process_post(post):
    # 공유수
    if 'shares' not in post:
        post['count_shares'] = 0
    else:
        post['count_shares'] = post['shares']['count']
        del post['shares']

    # 전체 리액션 수
    if 'reactions' not in post:
        post['count_reactions'] = 0
    else:
        post['count_reactions'] = post['reactions']['summary']['total_count']
        del post['reactions']

    # 전체 커맨트 수
    if 'comments' not in post:
        post['count_comments'] = 0
    else:
        post['count_comments'] = post['comments']['summary']['total_count']
        del post['comments']

    # 한국시간으로 변경 KST = UTC + 9
    kst = datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    kst = kst + timedelta(hours=+9)
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')


def crawling(pagename, since, until, fetch=True):
    results = []

    # 결과를 파일로 저장하기
    filename = '%s/fb_%s_%s_%s.json' % (RESULT_DIRECTORY, pagename, since, until)

    if fetch:
        for posts in api.fb_fetch_posts(pagename, since, until):
            # 데이터가 없을 경우 패스~
            if posts is None:
                continue

            # 전처리 파싱
            for post in posts:
                pre_process_post(post)

            results += posts
        # print(results)

        with open(filename, 'w', encoding='utf8') as outfile:
            # ident : 여러행 sort_keys : 정렬, ensure : 아스키 사용
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

            # 폴더 경로 만들어주자~

    return filename


if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)
