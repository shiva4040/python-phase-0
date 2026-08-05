import sympy as sp
def f(x):
    # f= x**2 + 3*x
    return 2*x + 3
print("f(x)",f(2))
# f = (3*x + 1)**5
# print(sp.diff(f,x))
# f = x**2 * y + y**3
# print(sp.diff(f,x))
# print(sp.diff(f,y))

# Mini: Implement numerical gradient (finite difference) for f(x) = x^2 + 3x.
def f(x):
    return x**2 + 3*x
def numerical_gradient(f, x, h=1e-5):
    return (f(x+h)-f(x))/h
x =2
grad = numerical_gradient(f,x)
print("f(x)", f(x))
print("numerical_gradient", grad)