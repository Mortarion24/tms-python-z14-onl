def func_5(a, b):
    print('Гипотенуза=', ((a ** 2) + (b ** 2)) ** 0.5)
    print('Площадь=', (a * b) / 2)


x = int(input('катет х='))
y = int(input('катет у='))
func_5(x, y)