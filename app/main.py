class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person_data["name"], person_data["age"])
               for person_data in people]

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife \
                = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

    return persons
