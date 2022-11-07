import xml.etree.ElementTree as ET

tag1 = ET.Element("tag1")
tag2 = ET.SubElement(tag1, "tag2").text = "Animal"
tag3 = ET.SubElement(tag1, "tag3").text = "Domestic"
tag4 = ET.SubElement(tag1, "tag4")
tag4_1 = ET.SubElement(tag4, "tag4.1").text = "Cat"
tag4_2 = ET.SubElement(tag4, "tag4.2").text = "Persian"
tag5 = ET.SubElement(tag1, "tag5").text = "Iran"
tag6 = ET.SubElement(tag1, "tag6").text = "Male"
tag7 = ET.SubElement(tag1, "tag7").text = "2021.05.04"

ET.dump(tag1)

xml_string = "<motorvehicles><vehicle><registration_no>CBB1456</registration_no><make>Toyota</make><model>Premio</model></vehicle><vehicle><registration_no>PR2245</registration_no><make>Mazda</make><model>Bongo</model></vehicle><vehicle><registration_no>DE2115</registration_no><make>TATA</make><model>Sumo</model></vehicle><vehicle><registration_no>CAR7785</registration_no><make>Kia</make><model>Optima</model></vehicle></motorvehicles>"
root = ET.fromstring(xml_string)
[j.tag for i in root for j in i]

root.tag # 'motorvehicles'
for vehicle in root:
    for attr in vehicle:
        print(attr.tag, attr.text)

for vehicle in root:
    for attr in vehicle:
        if attr.tag == "registration_no" and attr.text == "DE2115":
            vehicle.find("make").text = "Nissan"
            vehicle.find("model").text = "Skyline"

for vehicle in root:
    for attr in vehicle:
        print(attr.tag, attr.text)

ET.dump(root) # great :))

for vehicle in root:
    for attr in vehicle:
        if attr.tag == "make" and attr.text == "Nissan":
            vehicle.find("registration_no").text