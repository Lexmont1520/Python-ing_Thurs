def PrintString(textLine):
    print(textLine)


def HyperFunc(func):
    func("Hello From PrintString")


print(type(PrintString))
HyperFunc(PrintString)

funcList = [PrintString, HyperFunc]
funcList[0]("Hello From FuncList")

print("\n\n\n\n")
funcDict ={PrintString:"Value for PrintStringFUnc()", HyperFunc:"Value for HyperFUnc()"}

print(funcDict[PrintString])

#funcList.sort()