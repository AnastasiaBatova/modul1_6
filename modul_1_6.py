# Словарь
my_dict={'Anastasia': 1999,'Sahsa': 1997,'Dasha': 2001}
print(my_dict)
print(my_dict['Anastasia'])
print(my_dict.get('Misha', 'такого имени нет в списке'))
my_dict.update({'Irina' : 1993,'Kolya' :2003})
print(my_dict)
del my_dict['Dasha']
print(my_dict)
# Множеста
my_set = {1,4,2,4,1,'a','a', 'a',12.6,12.6, 2, ('c',4), ('c',4)}
print(my_set)
my_set.add('b')
my_set.add('c')
print(my_set)
my_set.discard(4)
print(my_set)


