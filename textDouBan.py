from bs4 import BeautifulSoup
import requests
import lxml

url = ("https://movie.douban.com/subject/24860318/?from=showing")

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