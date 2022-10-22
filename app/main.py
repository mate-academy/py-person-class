class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people.update({self.name: self})


def create_person_list(people_list: list) -> list:
    for dict_people in people_list:
        Person(dict_people["name"], dict_people["age"])
    Person.people["Ross"].wife = Person.people["Rachel"]
    Person.people["Rachel"].husband = Person.people["Ross"]
    person_list = [Person.people[key] for key in Person.people]
    return person_list
