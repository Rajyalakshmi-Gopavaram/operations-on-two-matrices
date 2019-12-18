#Importing numpy as np
import numpy as np
A = np.array(input("enter the 3*3 matrix A:"))
B=np.array(input("enter the 3*3 matrix B:"))
#addition of matrix A and B
print "Addition of matrix A and B:\n",np.add(A,B)
#Subraction of matrix A and B
print "Subraction of matrix A and B:\n",np.subtract(A,B)
#Multiplication of matrix A and B
print "Multiplication of matrix A and B:\n",np.matmul(A,B)
#Division of matrix A and B
print "Division of matrix A and B:\n",np.divide(A,B)
# Square of matrix A
print "Square  of A:\n", np.square(A)
# Square of matrix B
print "Square  of B:\n", np.square(B)
# Transpose of matrix A
print "Transpose of A:\n", np.transpose(A)
# Transpose of matrix B
print "Transpose of B:\n", np.transpose(B)
# Inverse of matrix A
print "Inverse matrix of A:\n", np.linalg.inv(A)
# Inverse of matrix B
print "Inverse matrix of B:\n", np.linalg.inv(B)
# Square root of matrix A
print "Square root matrix of A:\n", np.sqrt(A)
# Square root of matrix B
print "Square root matrix of B:\n", np.sqrt(B)
# Rank of a matrix A
print "Rank of A:", np.linalg.matrix_rank(A)
# Rank of a matrix B
print "Rank of B:", np.linalg.matrix_rank(B)
# Trace of matrix A
print "Trace of A:", np.trace(A)
# Trace of matrix B
print "Trace of B:", np.trace(B)
# Determinant of a matrix A
print "Determinant of A:", np.linalg.det(A)
# Determinant of a matrix B
print "Determinant of B:", np.linalg.det(B)


