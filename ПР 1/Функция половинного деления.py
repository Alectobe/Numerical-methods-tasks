def dichotomia_method(f, a, b, tol=1e-8, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна иметь разный знак на концах интервала")

    iterations = 0

    for _ in range(max_iter):
        c = (a + b) / 2
        iterations += 1

        if abs(f(c)) < tol or abs(b - a) < tol:
            return c, iterations

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2, iterations


def func(x):
    return x ** 2 - 5 * x + 6


root, iter_count = dichotomia_method(func, 2.5, 4)

print(f"Корень: {root:.6f}")
print(f"Число итераций: {iter_count}")
