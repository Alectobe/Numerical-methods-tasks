def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(fx) < tol:
            return x

        if dfx == 0:
            raise ValueError("Производная равна нулю, метод не применим")

        x = x - fx / dfx

    return x


def func(x):
    return x ** 2 - 5 * x + 6


def dfunc(x):
    return 2 * x - 5


x0 = 1
root = newton_method(func, dfunc, x0)
print(f"Корень: {root:.6f}")
