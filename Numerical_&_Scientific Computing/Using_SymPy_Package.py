import sympy as sp

x = sp.Symbol("x")

expression = x**2 + 10*x - 24
simplified = sp.simplify(expression)
print(simplified)

solution = sp.solve(expression,x)
print(solution)

