class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]

    for human in people:
        name = Person.people[human["name"]]
        husband = human.get("husband")
        wife = human.get("wife")

        if husband:
            name.husband = Person.people[husband]
        if wife:
            name.wife = Person.people[wife]

    return persons
