class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    result = [Person(data["name"], data["age"]) for data in people_list]

    for data in people_list:
        person_to_check = Person.people[data["name"]]

        if data.get("wife"):
            person_to_check.wife = Person.people[data["wife"]]

        if data.get("husband"):
            person_to_check.husband = Person.people[data["husband"]]

    return result
