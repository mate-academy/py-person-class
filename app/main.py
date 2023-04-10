class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    result = [Person(name=data.get("name"),
                     age=data.get("age")) for data in people]

    for person in people:
        if wife := person.get("wife"):
            Person.people[person["name"]].wife = (Person.people[wife])

        if husband := person.get("husband"):
            Person.people[person["name"]].husband = (Person.people[husband])

    return result
