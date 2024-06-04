class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    ls_people = [Person(person["name"], person["age"]) for person in people]
    for one_person in people:
        name = one_person["name"]
        if one_person.get("wife"):
            wife = one_person["wife"]
            Person.people[name].wife = Person.people[wife]
        if one_person.get("husband"):
            husband = one_person["husband"]
            Person.people[name].husband = Person.people[husband]
    return ls_people
