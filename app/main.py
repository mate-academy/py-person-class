class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    people_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    married_people = [
        person
        for person in people
        if person.get("wife") is not None
        or person.get("husband") is not None]

    for person in married_people:
        if person.get("wife") is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        else:
            Person.people[person["name"]].husband = (
                Person.people[person["husband"]]
            )

    return people_list
