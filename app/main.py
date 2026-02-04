class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(p["name"], p["age"]) for p in people]
    for index in range(len(people)):
        wife_name = people[index].get("wife")
        husband_name = people[index].get("husband")
        if wife_name:
            persons_list[index].wife = Person.people[wife_name]
        elif husband_name:
            persons_list[index].husband = Person.people[husband_name]
    return persons_list
