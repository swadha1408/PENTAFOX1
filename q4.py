def main():
    x = input("Enter the string: ")
    n = len(x)
    i = 0
    while i < n - 1:
        count = 1
        while (i < n - 1 and
               x[i] == x[i + 1]):
            count += 1
            i += 1
        i += 1
        print(x[i - 1] + str(count), end="")


if __name__ == "__main__":
    main()
