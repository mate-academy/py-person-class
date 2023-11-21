class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list:
    objects = Person.people

    for person in people:
        Person.people[person["name"]] = Person(
            name=person["name"],
            age=person["age"],
        )

        if person.get("wife") and person["wife"]:
            Person.people[person["name"]].wife = person["wife"]

        if person.get("husband") and person["husband"]:
            Person.people[person["name"]].husband = person["husband"]

    for person in objects:
        if hasattr(objects[person], "wife"):
            objects[person].wife = objects[objects[person].wife]

        if hasattr(objects[person], "husband"):
            objects[person].husband = objects[objects[person].husband]

    return list(objects.values())
