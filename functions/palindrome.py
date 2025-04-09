def palindrome(string) -> bool:
    if string == string[::-1]:
        return True
    else:
        return False


def main():
    string = input("文字列入力")
    result = palindrome(string)
    print(result)


if __name__ == "__main__":
    main()
