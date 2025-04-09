def prime_number() -> bool:
    input_value: int = input("数値入力")
    if int(input_value) == 2 or 1:
        return True
    for i in range(2, int(input_value)):
        if int(input_value) % i == 0:
            return False
            break
        else:
            return True


def main():
    result = prime_number()
    print(result)


if __name__ == "__main__":
    main()
