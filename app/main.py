class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"])
                   for person in people]

    for person in people:
        person_name = person.get("wife") or person.get("husband")
        if person_name is not None:
            if person.get("wife"):
                Person.people[person["name"]].wife = Person.people[person_name]
            if person.get("husband"):
                Person.people[person["name"]].husband = Person.people[
                    person_name
                ]

    return people_list
