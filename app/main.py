class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        human = Person(person["name"], person["age"])
        if "wife" in person and person["wife"]:
            for human2 in people:
                if person["wife"] == human2["name"]:
                    person_wife = Person(human2["name"], human2["age"])
                    person_wife.husband = human
                    human.wife = person_wife
        people_list.append(human)
    return people_list
