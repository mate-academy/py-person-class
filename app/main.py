class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_data["name"], person_data["age"]) for person_data in people]


    for person_data in people:
        if person_data.get("wife") is not None:
            Person.people[person_data["name"]].wife \
                = Person.people[person_data["wife"]]
        elif person_data.get("husband") is not None:
            Person.people[person_data["name"]].husband \
                = Person.people[person_data["husband"]]
    return person_list
