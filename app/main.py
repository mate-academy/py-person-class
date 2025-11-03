class Person:
    people = {}

    def __init__(self, name: str, age: float) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]
        for key, value in person_data.items():
            if key not in ["name", "age"]:
                if isinstance(value, str) and value in Person.people:
                    setattr(person, key, Person.people[value])
                elif value is not None:
                    setattr(person, key, value)

    return person_list
