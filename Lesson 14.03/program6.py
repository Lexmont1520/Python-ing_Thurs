emptyList = []
for i in range(0,1000000):
    if(i%2 == 0 ):
        emptyList.append(i)


#print(emptyList)

anotherList = [x for x in range(0,1000000) if (x%2 ==0)]
#print(anotherList)










cubeVol = lambda a : a**3
sphereVol = lambda r : (4/3)*3.14*(r**3)

def figSub(func1, func2, A,R):
    #if( func1(A) <= func2(R)):
    #    return True
    #else:
    #    return False
    return func1(A) <= func2(R)

print(figSub(cubeVol, sphereVol, 5, 2))