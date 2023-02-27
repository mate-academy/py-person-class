class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(person["name"], person["age"]))
    for person in people:
        class_people_person_name = Person.people.get(person["name"])
        if "wife" in person and person["wife"] is not None:
            class_people_person_name.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            class_people_person_name.husband = Person.people[person["husband"]]

    return people_list
