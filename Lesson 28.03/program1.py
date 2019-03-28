name = 'I am Batman and i can fly'
print(name)
new_name = name.lower()
print(new_name)

temp = {}

for i in new_name:

    print(i)
    temp[i] = temp.get(i,0)+1

print(temp)


empty_List = []
for key,val in temp.items():
    empty_List.append((val,key))

empty_List.sort(reverse = True)
for i in empty_List:
    print(i)