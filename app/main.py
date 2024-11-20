class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    for i in people:
        Person(i["name"], i["age"])

    for i in people:
        if i.get("wife") is not None:
            current_person = Person.people[i["name"]]
            wife = Person.people[i["wife"]]
            current_person.wife = wife
        if i.get("husband") is not None:
            current_person = Person.people[i["name"]]
            husband = Person.people[i["husband"]]
            current_person.husband = husband

    return list(Person.people.values())
