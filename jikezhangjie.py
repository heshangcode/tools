import http.client
import json


def extract_article_titles(data):
    titles = []

    # 递归遍历 JSON 数据
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'article_title':
                titles.append(value)
            else:
                titles.extend(extract_article_titles(value))
    elif isinstance(data, list):
        for item in data:
            titles.extend(extract_article_titles(item))

    return titles

conn = http.client.HTTPSConnection("time.geekbang.org")
payload = json.dumps({
  "cid": 313,
  "size": 100,
  "prev": 0,
  "order": "earliest",
  "sample": False,
  "chapter_ids": [
    "1430",
    "1431",
    "1433",
    "1459",
    "1460",
    "1461",
    "1462",
    "1463",
    "1464"
  ]
})
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Cookie': 'MEIQIA_TRACK_ID=23qdirD0vLgpRfQxo4q2Sxk39S9; MEIQIA_VISIT_ID=24HD1q4XCtzEWwWcSr8Ss4cUAyy; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221703256%22%2C%22first_id%22%3A%2217e6a94f9a0785-07c6a6e8a42f02-15522e2e-3686400-17e6a94f9a19e9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Faccount.geekbang.com%2F%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Ftime.geekbang.org%2Fdashboard%2Fcourse%22%2C%22%24latest_utm_source%22%3A%22geektime%22%2C%22%24latest_utm_medium%22%3A%22app%22%2C%22%24latest_utm_term%22%3A%22zeus7N1US%22%2C%22%24latest_utm_campaign%22%3A%22linghang%22%7D%2C%22%24device_id%22%3A%2217e6a94f9a0785-07c6a6e8a42f02-15522e2e-3686400-17e6a94f9a19e9%22%7D; mantis5539=f1f538f0962a4cf68461d5cc8906981d@5539; LF_ID=fc496ad-ead55b0-53624be-1226e01; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221703256%22%2C%22first_id%22%3A%2217e6a94f9a0785-07c6a6e8a42f02-15522e2e-3686400-17e6a94f9a19e9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fpromo.geekbang.org%2Factivity%2Fstudent-certificate%3Futm_source%3Dgeektime%26utm_medium%3Dcaidanlan1%22%2C%22%24latest_utm_source%22%3A%22geektime%22%2C%22%24latest_utm_medium%22%3A%22caidanlan1%22%2C%22%24latest_utm_term%22%3A%22zeus7N1US%22%2C%22%24latest_utm_campaign%22%3A%22linghang%22%7D%2C%22%24device_id%22%3A%2217e6a94f9a0785-07c6a6e8a42f02-15522e2e-3686400-17e6a94f9a19e9%22%7D; _ga=GA1.2.1186837961.1642465655; gksskpitn=74d1c1ca-a012-4365-a1b2-bc76a8341c75; _gcl_au=1.1.384065454.1688907837; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1690101400; Hm_lvt_59c4ff31a9ee6263811b23eb921a5083=1690101400; _tea_utm_cache_20000743={%22utm_source%22:%22geektime%22%2C%22utm_campaign%22:%22zhannei%22%2C%22utm_term%22:%22banner%22%2C%22utm_content%22:%22article%22}; _ga_MTX5SQH9CV=GS1.2.1691367423.3.1.1691368193.0.0.0; GCID=3e14b8f-e053865-5ce7ba8-29f8412; _ga_JW698SFNND=GS1.2.1691629582.7.1.1691629583.0.0.0; gk_process_ev={%22count%22:2%2C%22utime%22:1691629583357%2C%22referrer%22:%22https://time.geekbang.org/column/article/89050%22%2C%22target%22:%22page_geektime_login%22%2C%22referrerTarget%22:%22page_geektime_login%22}; GRID=3e14b8f-e053865-5ce7ba8-29f8412; GCESS=BgYEGK20LAwBAQQEAI0nAAEIWP0ZAAAAAAAJAQEFBAAAAAAIAQMCBBM41GQKBAAAAAADBBM41GQLAgYADQEBBwTvvHAf; __tea_cache_tokens_20000743={%22web_id%22:%227253803848563875854%22%2C%22user_unique_id%22:%221703256%22%2C%22timestamp%22:1692060930541%2C%22_type_%22:%22default%22}; _gid=GA1.2.2000871316.1692316284; _gat=1; Hm_lpvt_59c4ff31a9ee6263811b23eb921a5083=1692403491; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1692403491; __tea_cache_tokens_20000743={%22web_id%22:%227253803848563875854%22%2C%22user_unique_id%22:%221703256%22%2C%22timestamp%22:1692403490969%2C%22_type_%22:%22default%22}; _ga_03JGDGP9Y3=GS1.2.1692403429.26.1.1692403491.0.0.0; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1692403509|1692403427',
  'DNT': '1',
  'Origin': 'https://time.geekbang.org',
  'Referer': 'https://time.geekbang.org/column/article/659358?cid=100052601',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
  'X-GEEK-REQ-ID': 'ca71b54b214549aabad7c18ac9ad891e@1@web',
  'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}
conn.request("POST", "/serv/v1/column/articles", payload, headers)
res = conn.getresponse()
data = res.read()
article_titles = extract_article_titles(json.loads(data.decode("utf-8")))
# 遍历打印article_titles
for title in article_titles:
    # 去掉 title 里的空格再打印
    print(title.replace(' ', ''))