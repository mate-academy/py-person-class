class Person:
    person = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.person[self.name] = self


def create_person_list(people: list) -> list:
    for i in people:
        Person(i["name"], i["age"])
    for i in people:
        person_instance = Person.person[i["name"]]

        if i.get("husband"):
            person_instance.husband = Person.person[i["husband"]]

        if i.get("wife"):
            person_instance.wife = Person.person[i["wife"]]

    return list(Person.person.values())
