import random

def main():
    x = input("Enter transmit Message: ")
    x = x[::-1]
    prefix = chr(random.randint(65, 122))
    print("Encoded Message: ", prefix+x)


if __name__=="__main__":
    main()