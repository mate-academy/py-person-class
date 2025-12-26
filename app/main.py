class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for human in people:
        name = human.get("name")
        age = human.get("age")

        person = Person(name, age)
        person_list.append(person)

    for human in people:
        current_person = Person.people.get(human["name"])
        current_wife = human.get("wife")
        if current_wife and current_wife in Person.people:
            current_person.wife = Person.people[current_wife]

        current_husband = human.get("husband")
        if current_husband and current_husband in Person.people:
            current_person.husband = Person.people[current_husband]

    return person_list
