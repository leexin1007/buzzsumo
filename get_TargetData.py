import requests
from get_cookie import *
'''
从get_cookie包拿取cookie进行requests请求
'''


def search_trend(search_keyword, search_count):
    url = 'https://app.buzzsumo.com/search/trends'
    cookie_num = demo()
    cookies = {'session_buzzsumo': cookie_num}
    headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
               'Host': 'app.buzzsumo.com',
               'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
               'x-csrf-token': 'MkqYwTCKBO41ZnNIkbbQUJ5x9zPZuxx8Hme8U4tZ',
               'accept': 'application/json, text/javascript, */*; q=0.01',
               'cache-control': 'no-cache',
               'x-requested-with': 'XMLHttpRequest',
               'x-vue-route-name': 'trending',
               'referer': 'https://app.buzzsumo.com/discover/trending',
               'accept-language': 'zh-CN,zh;q=0.9'}
    params = (('topic', search_keyword),
              ('hours', '24'),
              ('count', search_count),
              ('result_type', 'trending_now'),
              ('ignore', 'false'),
              ('domains', 'youtube.com'),
              ('language', 'en'))

    response = requests.get(url, headers=headers, params=params, cookies=cookies)
    # 判断请求网页状态码
    if response.status_code == 200:
        response_json = response.json()
        limit = response_json.get("limit", False)
        if not limit:
            results = response_json.get("results")
            print("本次查询，总条数为："+str(len(results)))
        else:
            print("limit is true")
    return True


def search_topic(search_keyword, begin_date, end_date, page):
    url = 'https://app.buzzsumo.com/search/articles'
    cookie_num = demo()
    cookies = {'session_buzzsumo': cookie_num}
    headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
               'Host': 'app.buzzsumo.com',
               'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
               'x-csrf-token': 'MkqYwTCKBO41ZnNIkbbQUJ5x9zPZuxx8Hme8U4tZ',
               'accept': 'application/json, text/plain, */*',
               'cache-control': 'no-cache',
               'x-requested-with': 'XMLHttpRequest',
               'x-vue-route-name': 'web',
               'referer': 'https://app.buzzsumo.com/content/web',
               'accept-language': 'zh-CN,zh;q=0.9'}
    params = (('type', 'articles'),
              ('result_type', 'total'),
              ('begin_date', begin_date),
              ('end_date', end_date),
              ('language', 'en'),
              ('min_words', '750'),
              ('q', search_keyword),
              ('search', 'true'),
              ('page', page))
    response = requests.get(url, headers=headers, params=params, cookies=cookies)
    if response.status_code == 200:
        response_json = response.json()
        limit = response_json.get("limit", False)
        if not limit:
            total_page = response_json.get("total_pages")
            total_results = response_json.get("total_results")
            print("本次查询，总条数为："+str(total_results))
            if page != total_page:
                page += 1
                search_topic(search_keyword, begin_date, end_date, page)
            else:
                return True
        else:
            print("limit is true")
    return True


if __name__ == '__main__':
    # trend数据 (可以考虑遍历一个目标数据)
    search_keyword = 'keyword'  # 词库|话题库
    search_count = 1  # page数
    search_trend(search_keyword, search_count)

    # search数据
    search_keyword = "topic"    # 搜索词库
    begin_date = "May 10 2022"  # 时间
    end_date = "Jun 10 2022"
    page = 1
    search_topic(search_keyword, begin_date, end_date, page)


