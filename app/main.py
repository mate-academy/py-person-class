class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    peoples_lst = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife") is not None:
            name_give_w = Person.people[person.get("wife")]
            Person.people[person.get("name")].wife = name_give_w
        if person.get("husband") is not None:
            name_give_h = Person.people[person.get("husband")]
            Person.people[person.get("name")].husband = name_give_h

    return peoples_lst
