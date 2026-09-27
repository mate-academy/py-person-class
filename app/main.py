class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list) -> list:
    buff = []
    for item in people:
        person = Person(item["name"], item["age"])
        buff.append(person)

    for item in people:
        person = Person.people[item["name"]]

        if item.get("wife") is not None:
            person.wife = Person.people[item["wife"]]

        if item.get("husband") is not None:
            person.husband = Person.people[item["husband"]]

    return buff
    pass
