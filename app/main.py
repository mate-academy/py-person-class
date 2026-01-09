class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    for i in people:
        name = i["name"]
        age = i["age"]
        Person(name, age)

    for i in people:
        glob = Person.people[i["name"]]
        if i.get("wife"):
            glob.wife = Person.people[i["wife"]]
        if i.get("husband"):
            glob.husband = Person.people[i["husband"]]

    return list(Person.people.values())
