def main():
    x = list(map(int,input().split(",")))
    decode = ""
    for num in x:
        decode += chr(num+64)
    print("Decoded message: ", decode)


if __name__ == "__main__":
    main()
