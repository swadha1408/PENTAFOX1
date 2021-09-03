def main():
    flag = False
    print("Enter array elements: ")
    arr = list(map(int, input().split(" ")))
    x = int(input("Enter Sum: "))
    for val in arr:
        if x-val in arr and x-val != val:
            print(val, x-val)
            flag = True
            break
    if not flag:
        print("No Pairs Found")


if __name__=="__main__":
    main()