class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    people_instances = []
    for person in people:
        person2 = Person(person["name"], person["age"])
        people_instances.append(person2)

    for person in people:
        anet = Person.people[person["name"]]
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            anet.wife = wife
        elif person.get("husband"):
            husband = Person.people[person["husband"]]
            anet.husband = husband

    return people_instances
