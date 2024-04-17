class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list[Person]:
    humans = []
    for person in people:
        human = Person(person["name"], person["age"])
        humans.append(human)
        if person.get("wife"):
            human.wife = person["wife"]
        elif person.get("husband"):
            human.husband = person["husband"]
    for index, human in enumerate(humans):
        if hasattr(human, "wife"):
            human.wife = Person.people[human.wife]
        elif hasattr(human, "husband"):
            human.husband = Person.people[human.husband]
    return humans
