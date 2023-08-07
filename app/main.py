class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_instance()
        self.people[name] = self

    def add_instance(self) -> None:
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = []
    for i in people:
        name_instance = Person(i["name"], i["age"])  # The layout of each instance
        persons_list.append(name_instance)
    for x in people:
        if x.get("wife"):
            Person.people[x["name"]].wife = Person.people[x["wife"]]
        if x.get("husband"):
            Person.people[x["name"]].husband = Person.people[x["husband"]]

    return persons_list
