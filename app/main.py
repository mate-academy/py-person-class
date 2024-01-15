class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(name=person["name"], age=person["age"])
                   for person in people]

    for person in people:
        human = Person.people[person["name"]]
        if "wife" in person:
            if person["wife"]:
                human.wife = Person.people.get(person.get("wife"))
        elif "husband" in person:
            if person["husband"]:
                human.husband = Person.people.get(person.get("husband"))

    return person_list
