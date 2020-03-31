import requests
import logging
import pytest
import json


class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    url = 'https://testerhome.com/api/v3/topics.json?limit=2'

    def test_get(self):
        r = requests.get(self.url)
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))

    def test_post(self):
        r = requests.post(self.url, params={"a": 1, "b": "string corntent"},
                          proxies={"https": "http://127.0.0.1.7778",
                                   "http": "http:127.0.0.1:7778"},
                          verify=False)
        logging.info(r.url)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))

    def test_cookies(self):
        pass

    def test_xueqiu_quote(self):
        url = "https://stock.xueqiu.com/v5/stock/portfollio/stock/list.json?"
        r = requests.get(url,
                         params={})

