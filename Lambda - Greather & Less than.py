def ChkPrime(no):
    if no % 2==0:
        return True
    else:
        return False

def Filter(arr):
    brr = []
    for i in range(len(arr)):
        if ChkPrime(arr[i]) == True:
            brr.append(arr[i])
    return brr

def main():
    arr = []
    print("Enter Number Of Elements you want:-")
    size = int(input())

    for i in range(size):
        print("Number:-",i+1)
        no = int(input())
        arr.append(no)
    print("List of your entered data:-",arr)

    data = Filter(arr)
    print("After Filtering Data:-",data)

    newdata=list(filter(lambda num: (num < 30), arr))
    print("Lambda with greather:-",newdata)

    newdata1 = list(filter(lambda num: (num > 20), arr))
    print("Lambda with lessthan:-", newdata1)

if __name__ =="__main__":
    main()