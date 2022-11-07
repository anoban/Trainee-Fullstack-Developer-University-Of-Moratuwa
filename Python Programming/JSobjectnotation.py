import json

# here's a dummy JSON object!
json_obj = {"Name":"Jennifer Lawrence",
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

# serializing a JSON object
json_str = json.dumps(json_obj)
type(json.dumps(json_obj)) # a string!!
# serializing turns a JSON object into a string
json_str

# deserializing turns a string into JSON object!
json.loads(json_str)
type(json.loads(json_str)) # a dictionary!!



# kwargs for serialization

json.dumps([1,2,3,4, {"Name":"Lucy","Age":26}], separators = (",", ";"))
json.dumps([1,2,3,4, {"Name":"Lucy","Age":26}], separators = ("-", ";"))
json.dumps([1,2,3,4, {"Name":"Lucy","Age":26}], separators = ("-|-", "--||--"))

json.dumps([1,89,3,62,9,351,6,0,41, {"Name":"Lucy","Age":26}], separators = (":",","), sort_keys = True)
json.dumps([1,89,3,62,9,351,6,0,41, {"Name":"Lucy","Age":26}], separators = (":",","), sort_keys = True, indent = 2)