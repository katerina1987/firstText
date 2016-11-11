from bs4 import BeautifulSoup
import requests
import lxml

urls = ["https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}".format(str(i)) for i in range(20,200,20)]

for single_url in urls:
    # print(single_url)

# def ger_url_link(url,dataUrl = None):
    '''
    urlData=requests.get(single_url)

    soups = BeautifulSoup(urlData.text,"lxml")
    dataUrl = []
    for urlLink in soups:
        dataUrl = {
             "urlLink":soups.select("url")
        }
        print(dataUrl)
    '''

dataUrl = ["https:\/\/movie.douban.com\/subject\/26628357\/","https:\/\/movie.douban.com\/subject\/3868141\/","https:\/\/movie.douban.com\/subject\/26592040\/"]
dataUrlSplits = []
for i in dataUrl:

    afterUrl = i.split("\/", 5)
    urlSplit = ""
    for i in range(0, 5):
        urlSplit += afterUrl[i] + "/"
    dataUrlSplits.append(urlSplit)
print(dataUrlSplits)


def get_data(url,data = None):
    wbData = requests.get(url)

    soup = BeautifulSoup(wbData.text,"lxml")

    titles = soup.select("#content > h1 > span")
    years = soup.select("#content > h1 > span.year")
    prices = soup.select("#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong")
    evaluationNumbers = soup.select("#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > div > div.rating_sum > a > span")
    # print(titles,years,prices,evaluationNumbers)

    for title, year, price, evaluationNumber in zip(titles,years,prices,evaluationNumbers):
        data = {
            "title": title.get_text(),
            "year" : year.get_text(),
            "price": price.get_text(),
            "evaluationNumber": evaluationNumber.get_text()
        }
        print(data)

for  i in dataUrlSplits:
    get_data(i)




# for single_url in urls:
#     ger_url_link(single_url)