class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for bio in people:
        Person(bio["name"], bio["age"])

    for bio in people:
        name = bio["name"]
        person = Person.people[name]
        if bio.get("wife"):
            for_wife = bio["wife"]
            person.wife = Person.people[for_wife]
        elif bio.get("husband"):
            for_husband = bio["husband"]
            person.husband = Person.people[for_husband]

    return [Person.people[bio["name"]] for bio in people]
