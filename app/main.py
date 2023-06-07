class Person:
    people = {}

    def __init__(self, name: str, age: int, *arg) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for pers in people:
        name = pers.get("name")
        age = pers.get("age")
        person = Person(name, age)
        person_list.append(person)
    for person in people:
        if person.get("wife") is not None:
            name_spouse = person.get("wife")
            Person.people[person["name"]].wife = Person.people[name_spouse]
        elif person.get("husband") is not None:
            name_spouse = person.get("husband")
            Person.people[person["name"]].husband = Person.people[name_spouse]

    return person_list
