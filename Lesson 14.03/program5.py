def Sum(a=2, b = 1):
    return a+b/(a-b)**(a/b)


a = lambda x=2,y=1: x+y/(x-y)**(x/y)

print("Define FUnc Name Results: ",Sum(2,3))
print("Lambda func results: ", a(2,3))

