class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        wife_name = people[i].get("wife")
        husband_name = people[i].get("husband")
        if wife_name is not None:
            person_list[i].wife = Person.people[wife_name]
        if husband_name is not None:
            person_list[i].husband = Person.people[husband_name]
    return person_list
