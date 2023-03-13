class Point(): #класс
    "Документация и сведения об этом классе. Да это делается вот так просто и вызывается методом __doc__"
    #его атрибуты
    color = 'red'  
    circle = 2

#вызовем документацию о классе
print(Point.__doc__)


# изменение значения атрибута класса
Point.color = 'black'


#Вывод всех атрибутов класса(и не только)  __dict__ - атрибут для вывода всего словоря
print(Point.__dict__ ) 


#Создания объекта(др. словами экземпляра) класса
a = Point()
b = Point()
'''     объект а и объект b это два разных независимых друг от друга объекта
Но значения атрибутов этих объектов не являются собственными, это всего лишь ссылка на атрибуты КЛАССА
     (если изменить значение атрибута класса, то это значение поменяется и во всех объектах)     
       Тип данных этих объектов = названию класса( в нашем случае type(a)==type(b)==Point )      '''
#создадим собственный атрибут для объекта
a.color = 'green'
'''Было a.__dict__ = {} т.к. объект имел только ссылки на аргументы класса
   Стало a.__dict__ = {"color": "green"}  теперь этот объект имеет собственный аргумент'''


#создадим новый атрибут КЛАССА(а не экземпляра) двумя способами
    #1
Point.type = 'disc'
    #2
setattr(Point, 'prop', 10) 
                        # setattr(obj, name, value)   !!!name - обязательно в виде строки!!!
                        # Если name = (уже сущесвтующий атрибут), то метод просто поменяет значение аргумента на указанное
'''Теперь у класса и всех его объектов появилось новое свойство(др.словами новый аргумент)'''
print(Point.__dict__)

#узнаем,существует ли аттрибут класса(или объекта). И если существует, то выведем его значение
getattr(Point, "dodopizza", False) #Вывод = Fasle
'''Если убрать третье условие (False), то при отсутствии аргумента выведет ошибку
Также есть еще один способ узнать о существовании атрибута'''
hasattr(Point, 'type') #True - если существует, False - если нет
hasattr(a,'circle') #Вывод = True! Да, даже если нет собственного аргумента, доступ к атрибуту все равно есть


#удалим какой-либо атрибут из метода или класса
'''Если удалить у объекта собственный аттрибут, то обект будет ссылаться на значение атрибута класса
                (если у удаленного атрибута объекта и атрибута класса одинаковые имена)     
    Есть два способа удалить:                   '''
#1
del Point.prop 
#2
delattr(Point, 'type') #delattr(obj, name)
'''Если мы удаляем не существующий (в собственном пространстве) атрибут, то мы получим ошибку'''
