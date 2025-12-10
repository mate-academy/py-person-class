class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list[dict]) -> list[Person]:
    # сначала создаём все объекты Person
    person_list = [Person(person_data["name"], person_data["age"]) for person_data in people_dicts]

    # потом связываем их через wife/husband
    for person_data in people_dicts:
        person_obj = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            person_obj.wife = Person.people[person_data["wife"]]

        if "husband" in person_data and person_data["husband"] is not None:
            person_obj.husband = Person.people[person_data["husband"]]

    return person_list
