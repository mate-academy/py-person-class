class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(peo["name"], peo["age"]) for peo in people]
    for hus in people:
        if "wife" in hus and hus.get("wife"):
            Person.people.get(hus.get("name")).wife = \
                Person.people[hus.get("wife")]
        if "husband" in hus and hus.get("husband"):
            Person.people.get(hus.get("name")).husband = \
                Person.people[hus.get("husband")]
    return person_list
