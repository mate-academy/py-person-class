class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    for data in people:
        Person(data.get("name"), data.get("age"))
    for person in people:
        human = Person.people.get(person.get("name"))
        human_wife = Person.people.get(person.get("wife"))
        human_husband = Person.people.get(person.get("husband"))
        if human_wife :
            human.wife = human_wife
        if human_husband:
            human.husband = human_husband

    return list(Person.people.values())
