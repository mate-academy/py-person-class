class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"]) for person in people]
    for personal_info in people:
        if personal_info.get("wife"):
            Person.people[personal_info["name"]].wife = \
                Person.people[personal_info["wife"]]
        if personal_info.get("husband"):
            Person.people[personal_info["name"]].husband = \
                Person.people[personal_info["husband"]]
    return persons_list
