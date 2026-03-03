class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for name in range(len(people)):
        wife_name = people[name].get("wife")
        husband_name = people[name].get("husband")
        if wife_name is not None:
            person_list[name].wife = Person.people[wife_name]
        if husband_name is not None:
            person_list[name].husband = Person.people[husband_name]
    return person_list
