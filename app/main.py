class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        person_name = Person.people[person["name"]]
        if person.get("wife"):
            person_name.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_name.husband = Person.people[person["husband"]]
        person_list.append(person_name)
    return person_list
    pass
