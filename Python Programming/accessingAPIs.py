import requests
BASE_URL = "https://google.com"

# HTTP GET requests
# sending a HTTP GET request with appended strings
resp = requests.get(BASE_URL + "/search?q=HTTP+requests")

# HTTP response from the webserver API endpoint is captured as resp!
# here the query string was "HTTP requests"
# this is equivalent to searching "HTTP requests" in google search bar!

resp.status_code # 200 success!
resp.json()

# HTTP POST requests
new_record = {"Name":"Jennifer Lawrence",
            "Qualification":{
                "Schooling":"NYC St.Peter's High School",
                "College":"York University",
                "Degree":"B.A Econ.",
                "Post-grad":"M.A",
                "Experience":{
                    "Sales-exec":14,
                    "Cashier":9,
                    "Overseer":22,
                    "Chief-of-staff":7
                }
            },
            "Personal":{
                "First_name":"Jennifer",
                "Middle_name":"Gonzolez",
                "Last_name":"Lawrence",
                "DOB":"1990-12-23",
                "Age":32,
                "Marital-status":"Divorced",
                "Children":0,
                "Job":"Accounts-clerk"
            }
          }

EMP_API = "https://somedummyurl.com"
resp = requests.post(EMP_API + "/employees", json = new_record)
# here we are sending a HTTP POST request to an API endpoint https://somedummyurl.com/employees to add a new employee
# since the API accepts new data in JSON format we format the POST data in JSON format!

resp.status_code
resp.json()

# HTTP PUT requests
update_record = {"Name":"Jennifer Lopez",
            "Qualification":{
                "Schooling":"NYC St.Peter's High School",
                "College":"York University",
                "Degree":"B.A Econ.",
                "Post-grad":"M.A",
                "Experience":{
                    "Sales-exec":14,
                    "Cashier":9,
                    "Overseer":22,
                    "Chief-of-staff":7
                }
            },
            "Personal":{
                "First_name":"Jennifer",
                "Middle_name":"Gonzolez",
                "Last_name":"Lawrence",
                "DOB":"1980-12-23",
                "Age":39,
                "Marital-status":"Divorced",
                "Children":2,
                "Job":"Accounts-clerk"
            }
          }
resp = requests.put(EMP_API + "/employees", json = update_record)
# PUT requests update the entire record! 
# will modify all the fields in the JSON object
# thus all information, even the ones that need not to be modified must be sent along the info that needs to be updated
# in order to keep an intact record

# HTTP PATCH requests
# these are used to update just one/few needed fields in a record!
patch_record = {"Name":"Jamine Lopez",
            "Personal":{
                "First_name":"Jamine",
                "Middle_name":"Gonzolez",
                "Last_name":"Lopez",
                "Marital-status":"Married",
                "Children":3
            }
          }
resp = requests.patch(EMP_API + "/employees", json = patch_record)
# notice that here, we are only including the fields that need change! not the entire record!!

# and there's HTTP DELETE requests to delete entire records!