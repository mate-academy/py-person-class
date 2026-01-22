class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if Person.people.get(person.get("wife")):
            Person.people.get(person.get("name")).wife =\
                Person.people.get(person.get("wife"))
        elif Person.people.get(person.get("husband")):
            Person.people.get(person.get("name")).husband = (
                Person.people.get(person.get("husband")))
    return list(Person.people.values())
