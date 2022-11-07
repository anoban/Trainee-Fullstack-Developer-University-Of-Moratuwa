import xml.etree.ElementTree as ET
import os
os.getcwd()
os.listdir()

# parsing the .xml document! 
txttree = ET.parse("dummy.xml")
root = txttree.getroot()

root.tag # 'store_items'
root.attrib # {} 

# let's do this again with attributes!
txttree = ET.parse("dummy.xml")
root = txttree.getroot()
root.tag # 'store_items'
root.attrib # {'date': '14/05/2022', 'time': '05:13 GMT+5.30', 'storeID': 'N06'}

# we can do the same with a string
xmlstring = open("dummy.xml", "r").read()
xmlstring # :))

ET.parse(xmlstring)
# did not work due to the presence of \n
xmlstr = ""
for string in xmlstring.split("\n"):
    xmlstr = xmlstr + string 
xmlstr

ET.parse(xmlstr) # did not work

strlist =  open("dummy.xml", "r").readlines()
strlist_clean = [word.replace("\n", "") for word in strlist]
str_clean = ""
for strng in strlist_clean:
    str_clean += strng
str_clean

ET.parse(str_clean)  # still not working

ET.parse(open("dummy.xml", "r", encoding = "utf-8").read().replace("\n", ""))
# fuck this crap

# extracting child node elements hierarchically
txttree = ET.parse("dummy.xml")
xmlDOM = txttree.getroot()

for tag in xmlDOM:
    for child in tag:
        print(tag.tag)
        for innerchild in child:
            print("{}: {}".format(innerchild.tag, innerchild.text))
        print("\n")

# we can store these info in a dictionary!

# tag based element extraction from .xml files
[element.tag for element in xmlDOM.iter(tag = "item")]
[element.text for element in xmlDOM.iter(tag = "name")]
[element.text for element in xmlDOM.iter(tag = "cpu")]
[i for i in xmlDOM.itertext()]

books = ET.parse("books.xml")
booktree = books.getroot()
booktree.tag # 'catalog'
booktree.text

bookdict = dict()
for book in booktree:
    propdict = dict()
    for props in book:
         propdict[props.tag.upper()] = props.text.replace("\n", "")
    bookdict[book.attrib.values().__str__()[-8:-3].upper()] = propdict

bookdict.keys()
bookdict.values()

# perfecto :))

for i in booktree:
    i.attrib.values().__str__()[-8:-3].upper()

[element.find("in_stock").attrib for element in xmlDOM.findall("store_items")] # didn't work

# modifying .xml files
books = ET.parse("books.xml")
booktree = books.getroot()
[(x.tag.upper(), x.text.replace("\n", "")) for i in booktree for x in i]

for tag in booktree:
    for child in tag:
        child.tag = child.tag.upper()

[j.tag for i in booktree for j in i]
# good! capitalized :))

books.write("capbooks.xml") # great :)))

