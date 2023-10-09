class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = age
    pass


def create_person_list(people: list) -> list:
    data = []
    for person in people:
        person["name"] = Person(person["name"], person["age"])
        if bool(person.get("wife")):
            person["name"].wife = person["wife"]
        if bool(person.get("husband")):
            person["name"].husband = person.get("husband")
        data.append(person["name"])
    return data
