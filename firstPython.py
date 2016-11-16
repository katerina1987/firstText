# import math
# def arg(*args):
#     if len(args)==0:
#       return 0.0
#     x = sum(args)*1.0/len(args)
#
# print arg(1,2)

#print arg()

# import json
# import requests
# import urllib
#
# urls = ["https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start={}".format(str(i)) for i in range(0,300,20)]
#
# for single_url in urls:
#     urlData =urllib.request.urlopen(single_url).read()
#     urlData = urlData.decode("utf-8")
#     s = json.loads(urlData)
#     for i in range(0,10):
#         urlData1 = s["subjects"][i]["url"]
#         print(urlData1)

import requests
import lxml
from bs4 import BeautifulSoup

url = "https://movie.douban.com/subject/25895257/"

wbData = requests.get(url)

soup = BeautifulSoup(wbData.text, "lxml")

titles = soup.select("#content > h1 > span")
years = soup.select("#content > h1 > span.year")
directors = soup.select("#info > span > span.attrs > a")
scriptwriters = soup.select("#info > span > span.attrs > a")
actors = soup.select("#info > span.actor > span.attrs > a")
types = soup.select("#info > span")
prices = soup.select("#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong")
evaluationNumbers = soup.select(
    "#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > div > div.rating_sum > a > span")
print(types)

# for title, year, director, scriptwriter, price, evaluationNumber in zip(titles, years, directors, scriptwriters, prices,
#                                                                         evaluationNumbers):
#     data = {
#         "title": title.get_text(),
#         "year": year.get_text(),
#         "director": director.get_text(),
#         "scriptwriter": list(scriptwriter[0].stripped_strings),
#         "price": price.get_text(),
#         "evaluationNumber": evaluationNumber.get_text()
#     }
#     print(data)




