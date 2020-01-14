import urllib.request

#urllib.request.urlopen("http://www.nepalstock.com/")
# urllib.request.urlopen("http://www.nepalstock.com/").geturl()
# urllib.request.urlopen("http://www.nepalstock.com/").read()
f=open("webpage.html","w+")
content=urllib.request.urlopen("http://www.nepalstock.com/").read()
# content
f.write(content.decode("utf-8"))
exit()