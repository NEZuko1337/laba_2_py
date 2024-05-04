from itertools import zip_longest


class Polynomial:
    def __init__(self, *args):
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, dict):
                self.coefficients = [0] * (max(arg.keys()) + 1)
                for degree, coeff in arg.items():
                    self.coefficients[degree] = coeff
            elif isinstance(arg, Polynomial):
                self.coefficients = arg.coefficients.copy()
            elif isinstance(arg, (list, tuple)):
                self.coefficients = list(arg)
            else:
                self.coefficients = arg

        else:
            self.coefficients = list(args)

    def __str__(self):
        terms = []
        if isinstance(self.coefficients, (int, float)):
            return str(self.coefficients)
        for degree, coeff in enumerate(self.coefficients):
            if coeff != 0:
                sign = "+" if coeff > 0 else "-"
                coeff = abs(coeff)
                if degree == 0:
                    terms.append(f"{sign} {coeff}")
                else:
                    if coeff == 1:
                        term = "x"
                    else:
                        term = f"{coeff}x"
                    if degree > 1:
                        term += f"^{degree}"
                    terms.append(f"{sign} {term}")
        if not terms:
            return "0"
        else:
            # Да, могу себе позволить решение в лоб
            smile_solution = " ".join(terms[::-1])
            return smile_solution if smile_solution[0] != "+" else smile_solution[1:].strip()

    def __repr__(self):
        coefficients = self.coefficients.copy()
        while coefficients and coefficients[-1] == 0:
            coefficients.pop()
        return f"Polynomial {coefficients}"

    def degree(self):
        """
        Поскольку длина списка коэффициентов многочлена на единицу больше его степени
        (так как индексация начинается с нуля), мы можем просто вернуть длину - 1
        :return: len_of_coefficients
        """
        if self == Polynomial(0, 0, 0):
            return 0
        return len(self.coefficients) - 1

    # Далее идет переопределение + - * (-) ==
    # zip_longest аналогична функции zip, но может работать с последовательностями разной длины.
    # Она возвращает итератор, который объединяет элементы из нескольких последовательностей в кортежи.
    # Если значения просто нет, то fillvalue - то значение которое поставится в соответсвие.
    def __add__(self, other):
        if isinstance(other, Polynomial):
            result_coeffs = [sum(pair) for pair in zip_longest(self.coefficients, other.coefficients, fillvalue=0)]
            return Polynomial(*result_coeffs)
        elif isinstance(other, (int, float)):
            result_coeffs = self.coefficients.copy()
            result_coeffs[0] += other
            return Polynomial(*result_coeffs)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Polynomial' and {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            result_coeffs = [pair[0] - pair[1] for pair in
                             zip_longest(self.coefficients, other.coefficients, fillvalue=0)]
            return Polynomial(*result_coeffs)
        elif isinstance(other, (int, float)):
            result_coeffs = self.coefficients.copy()
            result_coeffs[0] -= other
            return Polynomial(*result_coeffs)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Polynomial' and {type(other)}")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result_coeffs = [coeff * other for coeff in self.coefficients]
            return Polynomial(result_coeffs)
        elif isinstance(other, Polynomial):
            if isinstance(other.coefficients, int) and isinstance(self.coefficients, int):
                result_coeffs = [0] * (self.coefficients + other.coefficients)
                if len(result_coeffs):
                    for i, coeff1 in enumerate([self.coefficients]):
                        for j, coeff2 in enumerate([other.coefficients]):
                            result_coeffs[i + j] += coeff1 * coeff2
                else:
                    result_coeffs = [0]

            elif isinstance(self.coefficients, int):
                result_coeffs = [0] * (self.coefficients + len(other.coefficients))
                for i, coeff1 in enumerate([self.coefficients]):
                    for j, coeff2 in enumerate(other.coefficients):
                        result_coeffs[i + j] += coeff1 * coeff2

            elif isinstance(other.coefficients, int):
                result_coeffs = [0] * (len(self.coefficients) + other.coefficients)
                for i, coeff1 in enumerate(self.coefficients):
                    for j, coeff2 in enumerate([other.coefficients]):
                        result_coeffs[i + j] += coeff1 * coeff2

            else:
                result_coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
                for i, coeff1 in enumerate(self.coefficients):
                    for j, coeff2 in enumerate(other.coefficients):
                        result_coeffs[i + j] += coeff1 * coeff2
            return Polynomial(result_coeffs)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.coefficients == [other]
        elif isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        else:
            return False

    def __neg__(self):
        return Polynomial(*[-coeff for coeff in self.coefficients])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        result_coeffs = [-coeff for coeff in self.coefficients]
        result_coeffs[0] += other
        return Polynomial(*result_coeffs)

    def der(self, d=1):
        if d < 0:
            raise ValueError("d must be non-negative")
        result_coeffs = self.coefficients.copy()
        for _ in range(d):
            result_coeffs.pop(0)
            result_coeffs = [i * idx for idx, i in enumerate(result_coeffs, start=1)]
        return Polynomial(result_coeffs)

    def __call__(self, x):
        result = 0
        for degree, coeff in enumerate(self.coefficients):
            result += coeff * (x ** degree)
        return result

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.coefficients):
            raise StopIteration
        else:
            result = (self.index, self.coefficients[self.index])
            self.index += 1
            return result
