m = list(range(100))
m[58] = "Hi"
for i in m:
    try:
        print(i <= 100)
    except:
        print("TypeError")
        continue