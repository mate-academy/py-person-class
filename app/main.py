class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(new["name"], new["age"]) for new in people]
    for people_data in people:
        person = Person.people[people_data["name"]]
        if "wife" in people_data and people_data["wife"] is not None:
            person.wife = Person.people[people_data["wife"]]
        elif "husband" in people_data and people_data["husband"] is not None:
            person.husband = Person.people[people_data["husband"]]
    return people_list
