# bubble

nums = [6, 3, 2, 5, 1, 7, 4, 0]


def bubble_sort(list):
    length = len(list)

    for i in range(0, length - 1):
        print("outer i")
        print(i)
        print("---")

        for j in range(0, length - i - 1):
            # can reduce inner loop from checking right side
            # values as they have been sorted already
            print("inner j")
            print(j)
            print("------")
            if list[j] > list[j + 1]:
                # print("these are swapping:")
                # print(list[j])
                # print(list[j + 1])

                temp1 = list[j]
                temp2 = list[j + 1]

                list[j] = temp2
                list[j + 1] = temp1

    return list


result = bubble_sort(nums)
print(result)
