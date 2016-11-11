# import math
# def arg(*args):
#     if len(args)==0:
#       return 0.0
#     x = sum(args)*1.0/len(args)
#
# print arg(1,2)

#print arg()


url = "https:\/\/movie.douban.com\/subject\/26411201\/"

afterUrl = url.split("\/",5)
urlSplit = ""

for i in range(0,5):
    urlSplit += afterUrl[i]+"/"

print(urlSplit)
