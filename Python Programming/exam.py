Base_URL= "http://host1.open.uom.lk:8080"

new_record = {"productName":"Araliya Basmathi Rice",
        "description":"White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
        "category":"Rice",
        "brand":"CIC",
        "expiredDate":"2023.05.04",
        "manufacturedDate":"2022.02.20",
        "batchNumber":324567,
        "unitPrice":1020,
        "quantity":200,
        "createdDate":"2022.02.24"}
        
import requests
resp = requests.post(Base_URL + "/api/products/", json = new_record)
print(resp.status_code)

import requests
resp = requests.get("http://host1.open.uom.lk:8080/api/products/")
print(len(resp.json().get("data")))
resp.json()
resp.json().get("data")

import requests
update_rcrd = {"productName":"Araliya Basmathi Rice",
        "description":"White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
        "category":"Rice",
        "brand":"Araliya",
        "expiredDate":"2023.05.04",
        "manufacturedDate":"2022.02.20",
        "batchNumber":324567,
        "unitPrice":1020,
        "quantity":200,
        "createdDate":"2022.02.24"}
        
resp = requests.put("http://host1.open.uom.lk:8080/api/products/", json = update_rcrd)
print(resp.status_code)

update_rcrd = {"productName":"Araliya Basmathi Rice",
        "description":"White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
        "category":"Rice",
        "brand":"Araliya",
        "expiredDate":"2023.05.04",
        "manufacturedDate":"2022.02.20",
        "batchNumber":324567,
        "unitPrice":1020,
        "quantity":200,
        "createdDate":"2022.02.24"}
resp = requests.patch("http://host1.open.uom.lk:8080/api/products/", json = update_rcrd)
print(resp.status_code)

resp = requests.patch("http://host1.open.uom.lk:8080/api/products/567/", json = update_rcrd)
print(resp.status_code)