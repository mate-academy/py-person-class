class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        person = Person.people[human["name"]]
        wife_name = human.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        husband_name = human.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]
    return new_list
