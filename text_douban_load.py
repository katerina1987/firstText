from bs4 import BeautifulSoup
import requests
import lxml
import json
import urllib

urls = ["https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start={}".format(str(i)) for i in range(0,300,20)]

for single_url in urls:
    urlData =urllib.request.urlopen(single_url).read()
    urlData = urlData.decode("utf-8")
    s = json.loads(urlData)
    for i in range(0,10):
        urlData1 = s["subjects"][i]["url"]
print(urlData1)

def get_data(url,data = None):
    wbData = requests.get(url)

    soup = BeautifulSoup(wbData.text,"lxml")

    titles = soup.select("#content > h1 > span")
    years = soup.select("#content > h1 > span.year")
    directors = soup.select("#info > span > span.attrs > a")
    scriptwriters = soup.select("#info > span > span.attrs > a")
    prices = soup.select("#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong")
    evaluationNumbers = soup.select("#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > div > div.rating_sum > a > span")
    # print(titles,years,prices,evaluationNumbers)

    for title, year, director,scriptwriter, price, evaluationNumber in zip(titles,years,directors,scriptwriters,prices,evaluationNumbers):
        data = {
            "title": title.get_text(),
            "year" : year.get_text(),
            "director":director.get_text(),
            "scriptwriter":list(scriptwriter[0].stripped_strings),
            "price": price.get_text(),
            "evaluationNumber": evaluationNumber.get_text()
        }
        print(data)

# for  i in urlData1:
get_data(urlData1)









# for single_url in urls:
#     ger_url_link(single_url)