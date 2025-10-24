class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_status = Person.people[person["name"]]
        if person.get("wife") is not None:
            person_status.wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            person_status.husband = Person.people[person["husband"]]
        else:
            continue
    return result_list
