class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        class_people_person_name = Person.people.get(person["name"])
        if person.get("wife"):
            class_people_person_name.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            class_people_person_name.husband = Person.people[person["husband"]]

    return list(Person.people.values())
