


class Person:

    people = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people.append({[self.name]: Person(self.name, self.age)})

def create_person_list(people_list: list) -> list:
    for man in people_list:
        Person.people.append({man["name"]: Person(man["name"], man["age"])})

    return Person.people

people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"}
    ]

person_list = create_person_list(people)
print(isinstance(person_list[0], Person))

print(person_list)
print(Person.people)

