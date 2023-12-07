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
        if "wife" in person and person.get("wife") in Person.people:
            Person.people.get(person.get("name")).wife =\
                Person.people.get(person.get("wife"))
        elif ("husband" in person
              and person.get("husband") in Person.people):
            Person.people.get(person.get("name")).husband = (
                Person.people.get(person.get("husband")))
    return list(Person.people.values())
