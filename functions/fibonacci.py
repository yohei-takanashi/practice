def fibonacci():
    input_value = input("n番目までのフィボナッチ数列をリストにして返します")
    fibonacci_list = [1, 1]
    if int(input_value) == 1:
        return [1]
    if int(input_value) == 0:
        return []
    else:
        for i in range(2, int(input_value)):
            fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
        return fibonacci_list


def main():
    result = fibonacci()
    print(result)


if __name__ == "__main__":
    main()
