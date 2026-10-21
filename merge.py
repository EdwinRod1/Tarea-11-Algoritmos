
def merge(A, B, n, m):
    i = 0
    j = 0
    k = 0

    C = [0] * (n + m)

    while i < n and j < m:
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1

    while i < n:
        C[k] = A[i]
        i += 1
        k += 1

    while j < m:
        C[k] = B[j]
        j += 1
        k += 1

    return C


A = [11, 22, 23, 90]
B = [15, 17, 33, 42, 102]

n = len(A)
m = len(B)

C = merge(A, B, n, m)

print("Arreglo A:", A)
print("Arreglo B:", B)
print("Arreglo ordenado:", C)
