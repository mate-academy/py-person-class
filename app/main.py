class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if (
            person.get("wife") is None
            and person.get("husband") is None
        ):
            continue
        elif person.get("husband", None):
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband
        elif person.get("wife", None):
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
    person_list = []
    for person in people:
        person_list.append(Person.people[person["name"]])
    return person_list
