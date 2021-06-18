def main():
    print("Enter Expression Print Number:-")
    No = int(input())
    str = 1
    for i in range(No):
        for j in range(str,i+1):
            print(str)
            str = str + 1
if __name__ =="__main__":
    main()
