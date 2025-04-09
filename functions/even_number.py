def judge_even() -> bool:
    input_value = int(input())
    if input_value % 2 == 0:
        return True
    else:
        return False

def main():
    result = judge_even()
    print(result)


if __name__ == "__main__":
    main()