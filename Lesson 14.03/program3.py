#Object Notation

def Sum(a,b):
    return a+b

print(Sum(2,3))
print(Sum("LOl", "Kek"))


#Default Notation
def Sub(a = 0,b = 1):
    
    return a - b

print(Sub(2,3))
print(Sub(2,4))
print(Sub())
print(Sub(2))
print(Sub(b = 3, a = 1))

def Mult(a,b,c,d,e = 3,f = 3):
    return a*b*c*d*e*f
print(Mult(1,2,3,4))


def Division(a,b):
    return a/b

numeric = [1,2]
print(Division(numeric[0], numeric[1]))

print(Division(*numeric))

def InfinityArgs(*temp):
    return temp


print(InfinityArgs())
print(InfinityArgs(*["Alice", "BOb", "John"]))
print("Kek", "LOl", "John", 2, 3)


print("\n\n\n\n\n")
wordDict = {"name":"Derec", "surname":"Smith", "nationality":"Bulgarian"}
print(*wordDict)





##Static type
def StaticArgsFunc(a:int,b:int) -> int:
    return a+b

print(StaticArgsFunc(2,3))
print(StaticArgsFunc("Static","LOl"))

