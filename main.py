from polynomial import Polynomial

print(Polynomial([1, 2, 3]))
print(Polynomial({0: -3, 2: 1, 5: 4}))
poly = Polynomial({0: -3, 2: 1, 5: 4})
poly_copy = Polynomial(poly)
print(poly_copy)
print(Polynomial(0, 2, 0, 5))
print(repr(Polynomial(1, 2, 3, 0, 0, 0, 5, 0, 0)))
print(repr(Polynomial(2, 3)))
print(Polynomial(0, 2, 0, 5))
print(Polynomial([7, -2, 0, 1]))
print(Polynomial([7, -2, 0, -1]))
