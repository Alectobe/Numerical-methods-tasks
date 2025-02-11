def simplified_newton_method(f, df_fixed, x0, tol=1e-8, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)

        if abs(fx) < tol:
            return x

        x = x - fx / df_fixed

    return x


def func(x):
    return x ** 2 - 5 * x + 6


x0 = 2.5
df_fixed = 2 * x0

root = simplified_newton_method(func, df_fixed, x0)
print(f"Корень: {root:.6f}")
