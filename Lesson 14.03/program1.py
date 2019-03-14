a = 1
b = 5000

print(a+b)

s = a+b/(a-b)**(a/b)
c = 2
d = 700
s1 = c +d/(c-d)**(c/d)
print(s)
print(s1)

def SomethingFunc(arg1, arg2):
    result = arg1 + arg2/(arg1-arg2)**(arg1/arg2)
    return result

print("Func work results")
print(SomethingFunc(2,700))

