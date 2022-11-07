import requests
import json
from bs4 import BeautifulSoup

laughs_coconut = "https://scrape-sm1.github.io/site1/COCONUT%20market1super.html"
glomark_coconut = "https://glomark.lk/coconut/p/11624"
laughs_tissues = "https://scrape-sm1.github.io/site1/FLORA%20FACIAL%20TISSUES%202%20X%20160%20BOX%20-%20HOUSEHOLD%20-%20Categories%20market1super.com.html"
glomark_tissues = "https://glomark.lk/flora-facial-tissues-160s/p/10470"
laughs_bread = "https://scrape-sm1.github.io/site1/Crimson%20Bread%20Sliced%20market1super.com.html"
glomark_bread = "https://glomark.lk/top-crust-bread/p/13676"

page = requests.get(laughs_coconut)
page = requests.get(laughs_tissues)
page = requests.get(laughs_bread)

soup = BeautifulSoup(page.content, "html.parser")
soup.head
soup.contents[0]


# Laughs's items are Okay :)))))
soup.find_all(name = "div", attrs = "product-name")[0].text
soup.find_all(name = "span", attrs = "regular-price")[0].text
# price as a float! 
float(' Rs.115.00 '.strip().replace("Rs.", ""))

# let's work on Glomark items!
page = requests.get(glomark_coconut)
page = requests.get(glomark_tissues)
page = requests.get(glomark_bread)

soup = BeautifulSoup(page.content, "html.parser")
soup.head
open("glomark.html", "w", encoding = "utf-8").write(soup.prettify())
# we did it JOE :)))))

product = json.loads(soup.find_all(name = "script", type = "application/ld+json")[0].text)
product.get("description")
float(product.get("offers")[0].get("price"))
# YES SIRRRR :)))))))














for i in parsed_page.find_all("span"):
    print(i.tag, i.text, i.attrs)

page = requests.get(glomark_coconut)
parsed_page = BeautifulSoup(page.content, "html.parser")
parsed_page.text.replace("\n", "")
