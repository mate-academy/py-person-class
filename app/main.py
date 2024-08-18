class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        name = person["name"]
        age = person["age"]
        if name in Person.people:
            persona = Person.people[name]
        else:
            persona = Person(name, age)

        if "wife" in person and person["wife"]:
            if person["wife"] not in Person.people:
                persona.wife = Person(person["wife"], 0)
            else:
                persona.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            if person["husband"] not in Person.people:
                persona.husband = Person(person["husband"], 0)
            else:
                persona.husband = Person.people[person["husband"]]

        person_list.append(persona)

    return person_list
