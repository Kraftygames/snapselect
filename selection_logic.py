import random


def choose(lst, qty, selected=None):
    if selected is None:
        selected = []

    if len(lst) < qty:
        return selected

    available = [elem for elem in lst if elem not in selected]

    if len(available) >= qty:
        return random.sample(available, qty)

    return random.sample(lst, qty)


def main():
    print("hi")

    for i in range(10):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        picked = choose(lst=my_list, qty=2)

        for a in picked:
            print(a, end=", ")

        print()
    print("end")



if __name__ == '__main__':
    main()
