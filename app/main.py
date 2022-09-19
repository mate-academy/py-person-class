class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances_list = []
    for person in people:
        if 'wife' in person.keys() and person['wife'] is not None:
            pers = Person(person['name'], person['age'])
            pers.wife = person['wife']
            person_instances_list.append(pers)
        elif 'husband' in person.keys() and person['husband'] is not None:
            pers = Person(person['name'], person['age'])
            pers.husband = person['husband']
            person_instances_list.append(pers)
        else:
            pers = Person(person['name'], person['age'])
            person_instances_list.append(pers)

    for person in person_instances_list:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]
    return person_instances_list
