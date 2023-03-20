"""
https://contest.yandex.ru/contest/46355/problems/

"""


def _robot_steps(N: int) -> tuple[int, int]:
    COUNT_CONST_X = []
    for idx_x in range(N):
        COUNT_CONST_X.append((-1) ** (idx_x + 1))
        COUNT_CONST_X.append(0)

    COUNT_CONST_Y = []
    for idx_y in range(N):
        COUNT_CONST_Y.append(0)
        COUNT_CONST_Y.append((-1) ** (idx_y + 1))

    # list_out_x = []
    # list_out_y = []

    n = 0
    x = 0
    y = 0
    length = 1
    count_two = 0

    while n != N:
        for idx in range(N):
            if count_two == 2:
                count_two = 1
                length += 1
            else:
                count_two += 1
            for _ in range(int(length)):
                x += COUNT_CONST_X[idx]
                # list_out_x.append(COUNT_CONST_X[idx])
                y += COUNT_CONST_Y[idx]
                # list_out_y.append(COUNT_CONST_Y[idx])
                n += 1
                if n == N:
                    break

            if n == N:
                break
        if n == N:
            break
    return x, y


def _main():
    """
    Ф-ция для проверки раброты алгоритма на тестовых примерах из условия задачи.

    """
    has_error_global = False

    for val, expected in (
        (0, (0, 0)),
        (1, (-1, 0)),
        (2, (-1, -1)),
        (14, (0, -2)),
    ):
        res = _robot_steps(N=val)
        has_error = res != expected
        has_error_global |= has_error

        print(f'{val} -> {res} ', end='')

        if has_error:
            print(f'!= {expected}', end='')

        print()

    print('ERROR' if has_error_global else 'OK')


if __name__ == '__main__':
    exit(_main())
