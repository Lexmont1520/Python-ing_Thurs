

def swap(arr, id_1, id_2):
    t = arr[id_1]
    arr[id_1] = arr[id_2]
    arr[id_2] = t

def bubbleSort(arr, reversed = True, abs = True):
    if reversed == True:
        for P_num in range(len(arr)-1, 0, -1):
            for i in range(0,P_num,1):
                if arr[i] < arr[i+1]:
                    swap(arr, i, i+1)
    else:
        for P_num in range(len(arr)-1, 0, -1):
            for i in range(0,P_num,1):
                if arr[i] > arr[i+1]:
                    swap(arr, i, i+1)



a = [2,-1, 500, 100, -22, 43.1, 3.1415]
print(a)
bubbleSort(a, reversed= True)
print("Reversed True: ",a)
bubbleSort(a, reversed= False)
print("Reversed False :",a)