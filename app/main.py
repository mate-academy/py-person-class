class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []

    for person in people:
        man = Person(person.get("name"), person.get("age"))
        people_list.append(man)

    for person in people:
        for man in people_list:
            if man.name == person.get("name"):
                if person.get("husband") in Person.people:
                    man.husband = Person.people.get(person.get("husband"))
                if person.get("wife") in Person.people:
                    man.wife = Person.people.get(person.get("wife"))

    return people_list
