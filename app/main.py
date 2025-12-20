class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person['name'], person['age'])
        if person['wife']:
            wife_info = person['wife']
            new_person.wife = Person(wife_info['name'], wife_info['age'])
        elif person['husband']:
            husband_info = person['husband']
            new_person.husband = Person(husband_info['name'], husband_info['age'])
        person_list.append(new_person)
    return person_list