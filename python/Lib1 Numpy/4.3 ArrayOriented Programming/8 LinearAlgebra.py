import numpy as np


def main():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    # diag(): Return the diagonal elements or create a diagonal matrix
    diag_elements = np.diag(a)
    print(f"Diagonal Elements of A :{diag_elements}\n")

    diag_matrix = np.diag(diag_elements)
    print(f"Diagonal matrix form elements : \n{diag_matrix}\n")

    # dot(): Matrix multiplication
    dot_product = np.dot(a, b)
    print(f"Dot product of A and B\n {dot_product}\n")

    # trace(): Sum of the diagonal elements
    trace_sum = np.trace(a)
    print(f"Trace of A : {trace_sum}\n")

    # det(): Matrix determinant
    determinant = np.linalg.det(a)
    print(f"Determinant of A : {determinant}\n")

    # eig(): Eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(a)
    print(f"Eigenvalues  of a : \n {eigenvalues}")
    print(f"Eigenvectors of a : \n {eigenvectors}\n")

    # inv(): Inverse of a square matrix
    inverse_b = np.linalg.inv(b)
    print(f"Inverse of B: \n {inverse_b}\n")

    # pinv(): Moore-Penrose pseudo-inverse
    pinv_A = np.linalg.pinv(a)
    print(f"Moore-Penrose pseudo-inverse of A:\n{pinv_A}\n")

    # qr(): QR decomposition
    Q, R = np.linalg.qr(a)
    print(f"Q matrix from QR decomposition:\n {Q}")
    print(f"R matrix from QR decomposition:\n {R}\n")

    # svd(): Singular value decomposition
    U, S, Vt = np.linalg.svd(a)
    print(f"U matrix from SVD:\n{U} ")
    print(f"Singular values from SVD: {S}")
    print(f"Vt matrix from SVD:\n : {Vt}\n")

    # solve(): Solve the linear system Ax = b
    b = np.array([1, 2])
    x = np.linalg.solve(a, b)
    print(f"Solution to Ax = b: {x}\n")  # Output: [-3.  2.]

    # lstsq(): Least-squares solution to Ax = b
    x, residuals, rank, s = np.linalg.lstsq(a, b, rcond=None)
    print(f"Least-squares solution to Ax = b : {x}")


if __name__ == "__main__":
    main()
