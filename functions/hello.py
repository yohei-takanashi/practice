def hello():
    name = input()
    return f"こんにちは、{name} さん！"


def main():
    result = hello()
    print(result)


if __name__ == "__main__":
    main()
