class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"]) for person in people]
    for number in range(len(people)):
        if people[number].get("husband"):
            persons_list[number].husband \
                = persons_list[number].people[people[number]["husband"]]
        elif people[number].get("wife"):
            persons_list[number].wife \
                = persons_list[number].people[people[number]["wife"]]
    return persons_list
