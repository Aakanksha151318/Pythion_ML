def PrimeNO(no):
    if no % 2==0:
        return True
    else:
        return False

def PrimeFilter(arr):
    brr = []
    for i in range(len(arr)):
        if PrimeNO(arr[i]) == True:
            brr.append(arr[i])

    return brr

def PrimeMap(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] + 2
    return arr

def PrimeReduce(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] - 2
    return arr

def Reduce(arr):
    sum = 0
    for i in range(len(arr)):
        sum = arr[i] + sum
    return sum

def main():
    arr = []
    print("Enter Number of Elements:-")
    length = int(input())

    for i in range(length):
        print("Number is:-",i+1)
        no = int(input())
        arr.append(no)
    print("Your Enter Data Is:-",arr)

    data = PrimeFilter(arr)
    print("After Filtering Data:-",data)

    data1= PrimeMap(arr)
    print("After Filtering Data is MAP:-",data1)

    data2 = PrimeReduce(arr)
    print("After Filtering Data is REDUCE:-", data2)

    data3 =Reduce(arr)
    print("After REDUCE data Addition:-", data3)
if __name__=="__main__":
    main()