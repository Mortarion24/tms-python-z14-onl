x = int(input('x='))
y = int(input('y='))
list_1 = [x, y]
print('Среднее арифметическое=', sum(list_1)/len(list_1))
print('Среднее геометрическое=', (x*y)**(1/(len(list_1))))
