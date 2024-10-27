import cmath

def solution(a, b, c):
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + cmath.sqrt(D)) / (2 * a)
        x2 = (-b - cmath.sqrt(D)) / (2 * a)
        roots = (x1.real, x2.real)
    elif D == 0:
        x = -b / (2 * a)
        roots = (x,)
    else:
        return tuple()

    return tuple(sorted(roots))


if __name__ == "__main__":
    print(solution(a=1, b=6, c=5))  # (-5.0, -1.0)
    print(solution(a=1, b=4, c=4))  # (-2.0,)
    print(solution(a=1, b=6, c=45))  # ()
