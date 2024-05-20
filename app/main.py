class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for person in people:
        Person(person["name"], person["age"])

    for ppl in people:
        if "wife" in ppl and ppl["wife"]:
            Person.people[ppl["name"]].wife = Person.people[ppl["wife"]]
        if "husband" in ppl and ppl["husband"]:
            Person.people[ppl["name"]].husband = Person.people[ppl["husband"]]

    return list(Person.people.values())
