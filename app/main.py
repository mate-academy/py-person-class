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
            for person in humans[index:]:
                if human.wife == person.name:
                    human.wife = person
                    person.husband = human
                    break
        elif hasattr(human, "husband"):
            for person in humans[index:]:
                if human.husband == person.name:
                    human.husband = person
                    person.wife = human
                    break
    return humans
