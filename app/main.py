class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    [Person(name=person["name"], age=person["age"]) for person in people]
    for current_people in people:
        if current_people.get("wife") is not None:
            Person.people[current_people["name"]].wife = Person.people[
                current_people["wife"]
            ]
        elif current_people.get("husband") is not None:
            Person.people[current_people["name"]].husband = Person.people[
                current_people["husband"]
            ]
    return list(Person.people.values())
