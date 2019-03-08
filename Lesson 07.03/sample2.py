a = {"name":"Jack", "surname":"London"}
a["otchestvo"] ="Ivanovich"
print(a)

for i in a.keys():
    print(i)


for i in a.values():
    print(i)

for key, value in a.items():
    print(key, value)