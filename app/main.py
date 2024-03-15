class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    for person in people:
        human = Person(person["name"], person["age"])

        if person.get("wife"):
            human.wife = Person.people.get(person.get("wife"))
            if human.wife:
                human.wife.husband = human

        if person.get("husband"):
            human.husband = Person.people.get(person.get("husband"))
            if Person.people.get(person.get("husband")):
                human.husband.wife = human

    return list(Person.people.values())
