
def count_zeros(Number):
    count = 0
    num_str = str(Number)
    for i in num_str:
        if i == 0:
            count = count + int(i)
            return count


def main():
    ret = count_zeros(1020300)
    print(ret)


if __name__ == "__main__":
    main()