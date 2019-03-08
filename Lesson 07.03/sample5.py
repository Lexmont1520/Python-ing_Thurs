
name = {"Russia":["Moscow", "SPB"], "Germany" :["Koln", "Dresden"], "Italy":["Bergamo","Salerno"]}

temp = []

for key, value in name.items():
    temp.append( (value,key) )

temp.sort()

for i in temp:
    print(i)

  
