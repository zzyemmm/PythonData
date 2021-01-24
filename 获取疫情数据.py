
import requests
import json
from bs4 import BeautifulSoup
from pyecharts.charts import Map,Geo
import jsonpath

url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

response = requests.post(url=url,headers=headers)
home_page = response.text
# print(home_page)

# 提取数据
# 把json->dict
data = json.loads(home_page)
name = jsonpath.jsonpath(data,"$..name,confirm")
print(name)