class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    people_class_list = [
        Person(person["name"], person["age"]) for person in people
    ]
    for person in people:
        if person.get("wife", False) and person.get("wife") is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif (person.get("husband", False)
              and person.get("husband") is not None):
            Person.people[person["name"]].husband = (
                Person.people)[person["husband"]]

    return people_class_list
