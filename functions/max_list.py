def max_list():
    sorted_list = sorted(int(x) for x in input().split())
    return sorted_list[-1]


def main():
    result = max_list()
    print(result)


if __name__ == "__main__":
    main()
