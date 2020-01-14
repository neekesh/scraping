import urllib.request as urlreq


fetch_url = "http://www.nepalstock.com/"

print("Fetching ", fetch_url)

resp = urlreq.urlopen(fetch_url).read()
resp_string = resp.decode("utf-8")

with open("webpage2.html","w+") as f:
    f.write(resp_string)

print("Complete!")

