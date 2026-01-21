class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    total_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        list1 = Person(name, age)
        total_list.append(list1)

    for person in people:
        list1 = Person.people.get(person["name"])
        if person.get("husband") and person["husband"] is not None:
            list1.husband = Person.people.get(person["husband"])
        elif person.get("wife") and person["wife"] is not None:
            list1.wife = Person.people.get(person["wife"])
    return total_list
