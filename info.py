import requests
import lxml.html

html = requests.get("http://www.nepalstock.com.np/news/category/0")
doc = lxml.html.fromstring(html.content)
latest_news = doc.xpath('//div[@id="home-contents"]')


# news_title = latest_news[0].xpath('.//td')
table = latest_news[0].xpath('.//td[@class="alnleft"]')
# print(table)
# table   = doc.xpath('//*[@id="home-contents"]/table')[0]
# allRows = table.xpath('tr')

print(table)
# print(allRows)

for td in table:
    print(td.text_content())



************************************************************************************************************************

#     for td in data:
#         resp = {
#         'news_date' : data[0][1].text_content(),
#         'company_symbol' : data[1][1].text_content(),
#         'news_title' :data[2][1].text_content(),
#         'news_description' :data[3][1].text_content(),
#         'attachment' : data[4][1][0].get("href") 
#         }
#         if not "attachment" in resp:
#             resp['attachment'] = "empty"
        
#         else:
#             continue
#         # try:
#         #     attachment = data[4][1][0].get("href")
#         # except:
#         #     resp['attachment'] = "empty"
#         # else:
#         #     resp['attachment'] = attachment

#         print(i, json.dumps(resp, indent = 4))
#         break
#     input()
# exit()


#########################################################################################################


# # news_title = latest_news.xpath('//*[@id="content"]/table/tbody/tr[2]/td[2]')
# news_title = latest_news.xpath('.//td[@class="alnleft"]')
# # for td in news_title:
#     # print(td.text_content())
# stock_sym = latest_news.xpath('.//td[@class="alnright"]')
# # for td in stock_sym:
#     # print(td.text_content())
# date = latest_news.xpath('.//td[@class="alnright"]')
# # print(date)
# output = []
# for info in zip(news_title, stock_sym, date):
#     resp = {}
#     resp['title'] = info[0].text_content().strip()
#     # resp['symbol'] = info[1].text_content().strip()
#     # resp['date'] = info[2].text_content().strip()
#     output.append(resp)

# print(*output, sep = "\n")

