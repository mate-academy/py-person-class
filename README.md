# class Person

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start


У вас есть список диктов "люди", каждый дикт означает
**человек**, у него есть ключи: `имя`, `возраст`,
`жена`/`муж` - зависит от того, мужчина это или
женский. Все "имена" разные. Ключ
`жена`/`муж` может быть либо `Нет`, либо
имя другого человека.

Создайте класс «Человек». Его конструктор принимает
и хранить `имя`, `возраст` человека.
Этот класс также должен иметь атрибут class
`люди`, это дикт, который хранит `человек`
экземпляры по их `имени`. Конструктор должен
добавить элементы к этому атрибуту.

Напишите функцию `create_person_list`, эта функция
принимает список `люди` и возвращает список с
Экземпляры Person вместо dicts.

**Примечание:**

Если ключ **человека** `жена`/`муж` не
`Нет` - следует добавить `create_person_list`
атрибут `жена`/`муж` соответственно
своему экземпляру. Этот атрибут должен
быть ссылкой на экземпляр `Person` с `name`
то же, что и ключ `жена`/`муж` в словаре человека.


Example:
```python
people = [
    {'name': 'Ross', 'age': 30, 'wife': 'Rachel'},
    {'name': 'Joey', 'age': 29, 'wife': None},
    {'name': 'Rachel', 'age': 28, 'husband': 'Ross'}
]

person_list = create_person_list(people) 
isinstance(person_list[0], Person) # True
person_list[0].name == 'Ross'
person_list[0].wife is person_list[2] # True
person_list[0].wife.name == 'Rachel'

person_list[1].name == 'Joey'
person_list[1].wife
# AttributeError

isinstance(person_list[2], Person) # True
person_list[2].name == 'Rachel'
person_list[2].husband is person_list[0] # True
# The same as person_list[0]
person_list[2].husband.name == 'Ross'
person_list[2].husband.wife is person_list[2]  # True

Person.people == {
    'Ross': <__main__.Person object at 0x10c20ca60>,
    'Joey': <__main__.Person object at 0x10c180a00>,
    'Rachel': <__main__.Person object at 0x10c1804f0>
}
```
`Hint` - use `pytest` for testing