def sum_list():
    #list(map(int,input().split()))
    #list_number = (int(x)for x in input().split())
    #total = sum(list_number)
    total =sum(int(x) for x in input().split())
    return total


def main():
    result = sum_list()
    print(result)


if __name__ == "__main__":
    main()