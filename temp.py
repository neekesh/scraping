import requests
import lxml.html
import urllib.request
import os
import json
import psycopg2
import hashlib


if not os.path.exists("web.html"):
    fp = open("web.html", "w+")   
    content = urllib.request.urlopen("http://www.nepalstock.com.np/news/category/0").read()
    fp.write(content.decode("utf-8"))

data = open("web.html").read() 
doc = lxml.html.fromstring(data)
home_contents = doc.xpath('//div[@id="home-contents"]')[0]

allRows = home_contents[3][0][:]
# print(type(allRows))
# con = psycopg2.connect("postgresql:///test")
con = psycopg2.connect(
    database = "test",
    user = "refugee"
)
# print ("Opened database successfully")


cur = con.cursor()
cur.execute('''
create table if not exists demo_table(
news_date varchar(50), 
company_symbol varchar(7),
news_title varchar(100), 
news_description varchar(500), 
attachment varchar(200),
hashed char(64) unique
);''')

for i, tr in enumerate(allRows):
    try:
        if len(tr[4]) < 3: continue
    except:
        break

    innerRows = tr[4][1][0][1][1][0][:]
    # print(innerRows)
    resp = {}   
    for tr in innerRows:        
        # print(len(tr[1]) == 1 and tr[1][0].tag.__str__() == 'a' and tr[1][0].get('href'))
        if len(tr[1]) == 1 and tr[1][0].tag.__str__() == 'a':
            resp[tr[0].text_content()] = tr[1][0].get('href')
        else:
            resp[tr[0].text_content()] = tr[1].text_content().strip()
    # print("demo_table {} values {}".format(
    #     tuple(resp.keys()),
    #     tuple(resp.values())
    #     ))
    resp['Attachment'] = resp.get('Attachment')
    # hashed = hashlib.sha256(resp[tr[0].text_content()].encode('utf-8')).hexdigest()
    resp['hashed'] =  hashlib.sha256(resp[tr[0].text_content()].encode('utf-8')).hexdigest()
    print(i, json.dumps(resp, indent = 4))
    
    # try:
    #     cur.execute(
    #         "insert into demo_table values (%s, %s, %s, %s, %s, %s)",
    #         tuple(resp.values())
    #     )
    # except psycopg2.errors.UniqueViolation as e:
    #     # print(e)
    #     cur.rollback()
    #     continue

    try:
        cur.execute(
                "insert into demo_table values (%s, %s, %s, %s, %s, %s)",
                tuple(resp.values())
            )
        # con.commit()
    except psycopg2.errors.UniqueViolation as e:
        # get error code
        error = e.pgcode
        con.rollback()
        continue
    

    # print(resp["News Date"])

   
print("Records created succesfully!!!")

con.commit()
con.close()
# exit()
    
