class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_ls = []
    for person in people:
        people_ls.append(Person(person["name"], person["age"]))
    for person in people:
        new_person = Person.people[person["name"]]
        if person.get("wife"):
            new_person.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            new_person.husband = Person.people[person["husband"]]
    return people_ls
