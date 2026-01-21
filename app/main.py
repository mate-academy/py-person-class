
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_person = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        current_person = Person.people[person["name"]]
        if wife_name := person.get("wife"):
            his_wife = Person.people[wife_name]
            current_person.wife = his_wife
        if husband_name := person.get("husband"):
            her_husband = Person.people[husband_name]
            current_person.husband = her_husband

    return list_person
