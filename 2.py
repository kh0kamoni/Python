def main():
    numbers = list(map(int, input("Enter list of numbers seperated by space: ").split()))
    maximum = max(numbers)

    print("Maximum number", maximum)


if __name__ == "__main__":
    main()
    