class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(info["name"], info["age"])
                   for info in people]
    for person in people:
        if person.get("wife") is not None:
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        if person.get("husband") is not None:
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband
    return people_list
