class Person:
    # write your code here
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def create_person_list(peoples: list) -> list:
    return [Person(people["name"], people["age"]) for people in peoples]



peoples = [
    {'name': 'Ross', 'age': 30, 'wife': 'Rachel'},
    {'name': 'Joey', 'age': 29, 'wife': None},
    {'name': 'Rachel', 'age': 28, 'husband': 'Ross'}
]

person_list = create_person_list(peoples)




# for person in person_list:
#     print(f'{person.name} - {person.age} year')

