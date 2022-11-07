# requests can be used to send HTTP requests to web servers
import requests

# GET requests

webpage = requests.get("http://wallpaperswide.com/")

webpage.status_code # 200 OK
webpage.apparent_encoding # utf-8
webpage.content
webpage.url # 'http://wallpaperswide.com/'
webpage.text

# httpbin.org is a site that returns the client GET request params back to client :) 
dummy = requests.get("https://httpbin.org/get")
dummy.url
dummy.status_code
dummy.content
dummy.text # {"args": {},
            # "headers": {"Accept": "*/*",
            # "Accept-Encoding": "gzip, deflate", "Host": "httpbin.org", "User-Agent": "python-requests/2.27.1",
            # "X-Amzn-Trace-Id": "Root=1-627e2860-5efa25450057ea3e3e890cc8"},
            # "origin": "123.231.120.117", "url": "https://httpbin.org/get"}

# requesting non-existing webservers
bogus = requests.get("https://whatnotsite.io/somesrc?query=someshit")
#  Failed to establish a new connection: [Errno 11001]
# because the server we specified does not exist!

# requesting non-existent resources from existing webservers
page = requests.get("http://wallpaperswide.com/myfavwallpaper?query=hahaha")
page.status_code # 200
page.text

# searching google with the keyword "inspiron" shows the following URL in the address bar
# "https://www.google.com/search?client=firefox-b-d&q=inspiron"
# the string that folloes the ? mark are query params
# client=firefox-b-d means the request client is a Mozilla Firefox web browser
# q=inspiron means that the search string is "inspiron"
# an ampersand "&" concatenates adjacent query params

cpp = requests.get("https://google.com/search?q=cplusplus")
cpp.status_code
cpp.text

# dummy webscraping
plangs = ["Golang", "Julialang", "Perl", "R", "Python", "JavaScript", "Haskell", "C", "C++", "Rust", "Java", "Ruby", "C#", "F#"]
webqueries = dict()
for lang in plangs:
    page = requests.get("https://google.com/search?q=" + lang)
    webqueries[lang] = {"Status": page.status_code, "URL": page.url, "Encoding": page.encoding, "Text": page.text, "Content": page.content}
                            
webqueries.__sizeof__()
webqueries.keys()
webqueries.values()
webqueries["R"].keys()
webqueries["C++"].values()

# POST requests

dummypost = requests.post("https://httpbin.org/post", data = {"placeholder_key":"placeholder_value"})
dummypost.url
dummypost.text
dummypost.content