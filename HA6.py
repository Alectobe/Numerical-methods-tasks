import numpy as np


#  Метод непосредственного развёртывания
def direct_eigen_decomposition(A):
    eigenvalues = np.linalg.eigvals(A)

    # 2. Собственные векторы — для каждого λ решаем (A - λI)x = 0
    eigenvectors = []
    for lam in eigenvalues:
        mat = A - lam * np.eye(A.shape[0])
        u, s, vh = np.linalg.svd(mat)
        vec = vh[-1, :]
        eigenvectors.append(vec / np.linalg.norm(vec))

    return eigenvalues, np.array(eigenvectors).T


A = np.array([
    [2, 1, 0],
    [1, 2, 1],
    [0, 1, 2]
], dtype=float)

lambdas, vectors = direct_eigen_decomposition(A)
print("Собственные значения:", lambdas)
print("Собственные векторы (столбцы):\n", vectors)

# Метод итераций
def power_method(A, num_iter=100, tol=1e-8):
    n = A.shape[0]
    x = np.random.rand(n)
    x /= np.linalg.norm(x)

    last_lambda = 0.0
    for _ in range(num_iter):
        x_new = A @ x
        x_new_norm = np.linalg.norm(x_new)
        x_new /= x_new_norm
        lambda_ = x_new @ (A @ x_new)

        if np.abs(lambda_ - last_lambda) < tol:
            break
        x = x_new
        last_lambda = lambda_
    return lambda_, x


# Пример
lambda_max, vector_max = power_method(A)
print("Наибольшее по модулю собственное значение:", lambda_max)
print("Соответствующий собственный вектор:", vector_max)