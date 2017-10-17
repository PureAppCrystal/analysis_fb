# import analysis_fb.collection.crawler as crawler
import collection
import analyze
import visualize

'''
pagename = "jtbcnews"
since = "2017-10-01"
until = "2017-10-13"
'''


if __name__ == '__main__':
    items = [
        {"pagename": "jtbcnews", "since": '2017-01-01', "until": '2017-10-17'},
        {"pagename": "chosun", "since": '2017-01-01', "until": '2017-10-17'}
    ]

    # HTTP Error 500: Internal Server Error  -> 데이터가 없는것으로 유추 가능

    # collection
    for item in items:
        result_file = collection.crawling(**item, fetch=True)
        item['result_file'] = result_file

    # analysis
    for item in items:
        # print(item['result_file'])ㅣ
        data = analyze.json_to_str(item['result_file'], 'message')
        item['count'] = analyze.count_word_freq(data)

    # visualization
    for item in items:
        count = item['count']
        count_top50 = dict(count.most_common(50))
        file_name = '%s_%s_%s' % (item['pagename'], item['since'], item['until'])

        visualize.wordcloud(count_top50, file_name)

        visualize.graph_bar(
            values=list(count_top50.values()),
            ticks=list(count_top50.keys()),
            show_grid=False,
            file_name=file_name,
            show_graph=False
        )
