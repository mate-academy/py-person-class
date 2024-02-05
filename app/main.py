class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(
            Person(
                name=person["name"],
                age=person["age"]
            )
        )
    for person in people:
        if "wife" in person and person["wife"]:
            wife = Person.people[person["wife"]]
            wife.husband = Person.people[person["name"]]
            wife.husband.wife = wife
    return result
