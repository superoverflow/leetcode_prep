"""
Given an int array eg [1, 2, 3, 4, 5]
Return an array to give the rank correspondingly (5 being the largest number)
If there is a ties, the number appears earlier wins

"""


def solve(numbers: list[int]) -> list[int]:
    result = [len(numbers)] * len(numbers)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] >= numbers[j]:
                result[i] -= 1
            else:
                result[j] -= 1
    return result
