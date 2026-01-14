class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_instances = [Person(p["name"], p["age"]) for p in people]

    for person_dict in people:
        current_person = Person.people[person_dict["name"]]

        wife_name = person_dict.get("wife")
        if wife_name is not None:
            current_person.wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            current_person.husband = Person.people[husband_name]

    return person_instances
