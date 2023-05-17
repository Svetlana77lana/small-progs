"""
https://www.codewars.com/users/tomina-s/completed_solutions
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)

"""


def solution_1(s):
    exit_list = []
    tmp = []
    # for elem in s:
    for idx in range(len(s)):
        if idx % 2 == 0:
            tmp_str = s[idx] + s[idx+1]
            # tmp.append(s[idx])
            # tmp.append(s[idx+1])

            print('tmp', tmp_str)

            exit_list.append(tmp_str)
            print('exit_list', exit_list)
            tmp_str = ''

        # print(elem)

    print(s.split())
    # s.map(s)
    return exit_list


def solution_2(s):
    exit_list = []
    # for elem in s:
    str_length = len(s)
    # print(str_length)
    for idx in range(str_length):
        if idx % 2 == 0:
            if idx == str_length - 1:
                second = '_'
            else:
                second = s[idx+1]
            tmp_str = s[idx] + second
            # print('tmp', tmp_str)

            exit_list.append(tmp_str)
            # print('exit_list', exit_list)
            # tmp_str = ''

    # print(s.split())
    return exit_list


def solution(s):
    """solution_tom"""
    exit_list = []
    str_length = len(s)
    for idx in range(str_length):
        if idx % 2 == 0:
            second = '_' if idx == str_length - 1 else s[idx+1]
            tmp_str = s[idx] + second

            exit_list.append(tmp_str)

    return exit_list


def solution_dima(s):
    """dima"""
    iterationNum: int = int(0)
    res = []

    while iterationNum < len(s):

        length = len(s)
        if iterationNum < length - 1:
            str = s[iterationNum] + s[iterationNum + 1]
            res.append(str)
        elif (iterationNum == length - 1) & (length > 2):
            str = s[iterationNum] + "_"
            res.append(str)
        elif (iterationNum == length - 1) & (length < 2):
            str = s[iterationNum] + "_"
            res.append(str)
            break

        iterationNum += 2

    return res


import itertools


def solution_pasha(s):
    return [
        a + b
        for a, b
        in itertools.zip_longest(
            s[0::2],
            s[1::2],
            fillvalue='_',
        )
    ]


if __name__ == '__main__':
    inpuy_str = 'sdf'

    print(solution(inpuy_str))

