
class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person['name']
        age = person['age']
        human = Person(name, age)
        if person.get('wife') is not None:
            wife_name = person['wife']
            wife = Person.people.get(wife_name)
            human.wife = wife
        elif person.get('husband') is not None:
            husband_name = person['husband']
            husband = Person.people.get(husband_name)
            human.husband = husband
            husband.wife = human
        person_list.append(human)
    return person_list
