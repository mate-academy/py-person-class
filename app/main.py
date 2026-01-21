class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = []
    for human in people:
        person_list.append(Person(human["name"], human["age"]))
    for human in people:
        current_person = Person.people[human["name"]]
        if human.get("wife") is not None:
            current_person.wife = Person.people[human["wife"]]
        if human.get("husband") is not None:
            current_person.husband = Person.people[human["husband"]]
    return person_list
