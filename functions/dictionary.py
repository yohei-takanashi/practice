def add_dictionary(score_dict):
    for i in range(5):
        name = input("名前入力")
        score = input("成績入力")
        score_dict[name] = int(score)
    return score_dict


def average_dict(score_dict):
    return sum(score_dict.values()) / len(score_dict)


def main():
    score_dict = {}
    result = add_dictionary(score_dict)
    print(result)
    result2 = average_dict(score_dict)
    print(result2)


if __name__ == "__main__":
    main()
# input_dict :dict = for x in input().split()
