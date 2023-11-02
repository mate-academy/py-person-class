class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list[dict]) -> list:

    person_list = []

    for person in people:
        person = Person(person["name"], person["age"])
        person_list.append(person)

    for person in people:
        name = person["name"]
        spouse_name = person['wife' if 'wife' in person else 'husband']
        spouse = Person.people.get(spouse_name) if spouse_name else None
        Person.people[name].spouse = spouse

    return person_list
