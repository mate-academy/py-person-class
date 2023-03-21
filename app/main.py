class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = []
    for person_dict in people:
        person = Person(person_dict.get("name"), person_dict.get("age"))
        person_list.append(person)
    for person_dict in people:
        person = Person.people[person_dict.get("name")]
        if person_dict.get("wife") is not None:
            person.wife = Person.people[person_dict.get("wife")]
        elif person_dict.get("husband") is not None:
            person.husband = Person.people[person_dict.get("husband")]
    return person_list
