class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    for person_dict in people_data:
        if person_dict.get("name") not in Person.people:
            Person(person_dict.get("name"), person_dict.get("age"))

    for person_dict in people_data:
        current_person = Person.people.get(person_dict.get("name"))

        if person_dict.get("wife") is not None:
            current_person.wife = Person.people.get(person_dict.get("wife"))

        if person_dict.get("husband") is not None:
            current_person.husband = Person.people.get(person_dict.get("husband"))

    return [Person.people.get(p.get("name")) for p in people_data]
