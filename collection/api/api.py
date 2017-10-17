from urllib.parse import urlencode
from .json_request import json_request

ACCESS_TOKEN = '%s|%s' % ('1428253630556936', 'ba8f09769d565fc8646398885bdb20ae')
BASE_URL_FB_API = 'https://graph.facebook.com/v2.8'
LIMIT_REQUEST = 100


# 호출 url 폼 생성하기
def fb_gen_url(base=BASE_URL_FB_API, node='', **params):
    return '%s/%s/?%s' % (base, node, urlencode(params))


# 페이지의 아이디를 받아오기
def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename,
                     access_token=ACCESS_TOKEN)

    json_result = json_request(url=url)
    return json_result.get('id')


# post를 가져오는 url 생성 및 가져오기
def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename)+'/posts',
        fields='id,message,link,name,type,shares,created_time,\
                   reactions.limit(0).summary(true),\
                   comments.limit(0).summary(true)',
        since=since,
        until=until,
        limit=LIMIT_REQUEST,
        access_token=ACCESS_TOKEN)

    is_next = True

    while is_next:
        # url 호출, 페이징 정보 가져오기
        json_result = json_request(url=url)

        # 페이징 처리(다음 페이지 있는지 확인)
        paging = None if json_result is None else json_result.get('paging')
        url = None if paging is None else paging.get('next')
        is_next = url is not None

        # 데이터 보내기
        posts = None if json_result is None else json_result.get('data')
        yield (posts)
        # yield (json_result)




