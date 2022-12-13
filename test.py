# import cProfile
#
# import numpy as np
# import time
# def matmul_vanille(A: list[float], B: list[float]) -> list[float]:
#     result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
#     for i in range(len(A)):
#         for j in range(len(B[0])):
#             for k in range(len(B)):
#                 result[i][j] += A[i][k] * B[k][j]
#
# cProfile.run('matmul_vanille')





