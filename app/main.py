class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    i = 0

    for person in people:
        name = person["name"]
        age = person["age"]
        persona = Person(name, age)
        person_list.append(persona)

    for person in person_list:
        wife = people[i].get("wife")
        husband = people[i].get("husband")
        i += 1
        if wife:
            person.wife = Person.people[wife]
        elif husband:
            person.husband = Person.people[husband]

    return person_list
