
def employee(name,**data):
    print(name)
    print(data)
    print("*********************")
    for key,value in data.items():
        print(key,value)

#keyword variable args
employee("Girish",age="31",city="Mumbai",mobile="12345")
