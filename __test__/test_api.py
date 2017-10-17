from analysis_fb.collection.api import api


# url = api.fb_gen_url(pagename='jtbcnews', a=1, b=2, no=3, token='abc' )
# print(url)

# print(api.fb_name_to_id('jtbcnews'))

# api.fb_fetch_posts('jtbcnews', '2017-08-01', '2017-10-12')
# api.fb_fetch_posts(api.fb_name_to_id('chosun'), '2017-01-01', '2017-10-12')


for posts in api.fb_fetch_posts('jtbcnews', '2017-08-01', '2017-10-12'):
    print(posts)

