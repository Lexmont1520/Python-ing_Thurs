tupExamplt = tuple()
tupExamplt = ()

tupExampl2 = (2,3,4,5,6,7)
print(type(tupExampl2))

print(tupExampl2[2])

a = tupExampl2 + tupExampl2
print(a)


temp = []
for i in range(0,100):
    temp.append(i)

print(a + tuple(temp))