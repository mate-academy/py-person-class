class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = [Person(p["name"], p["age"]) for p in people]

    for i, person_dict in enumerate(people):
        wife_name = person_dict.get("wife")
        if wife_name:
            person_list[i].wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")
        if husband_name:
            person_list[i].husband = Person.people[husband_name]

    return person_list
