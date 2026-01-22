class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        human = Person(person["name"], person["age"])
        result.append(human)
        if person.get("wife"):
            human.wife = Person.people.get(person["wife"])
            if human.wife:
                human.wife.husband = human
        elif person.get("husband"):
            human.husband = Person.people.get(person["husband"])
            if human.husband:
                human.husband.wife = human
    return result
