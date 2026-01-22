class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    creatings = [Person(person["name"], person["age"]) for person in people]
    for persona in people:
        if persona.get("wife"):
            Person.people[persona["name"]].wife\
                = Person.people[persona["wife"]]
        if persona.get("husband"):
            Person.people[persona["name"]].husband\
                = Person.people[persona["husband"]]

    return creatings
