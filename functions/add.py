def add():
    a, b = (int(x) for x in input().split())
    return a + b


def main():
    result = add()
    print(result)


if __name__ == "__main__":
    main()
