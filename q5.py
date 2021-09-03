def main():
    x = input("Enter word-1: ")
    y = input("Enter word-2: ")
    common = set()
    for i in range(len(x)):
        if x[i] not in y:
            common.add(x[i])
    for i in range(len(y)):
        if y[i] not in x:
            common.add(y[i])

    print("Common Letters: ",common)

if __name__ == "__main__":
    main()