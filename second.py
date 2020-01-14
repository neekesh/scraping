import urllib.request as urlreq


fetch_url = "http://www.nepalstock.com.np/news/category/0"

print("Fetching ", fetch_url)

resp = urlreq.urlopen(fetch_url).read()
resp_string = resp.decode("utf-8")

with open("webpage3.html","w+") as f:
    f.write(resp_string)

print("Complete!")

