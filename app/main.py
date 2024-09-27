class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for name_person in people:
        if wife_name := name_person.get("wife"):
            Person.people[name_person["name"]].wife \
                = Person.people[wife_name]
            Person.people[name_person["name"]].wife.husband \
                = (Person.people)[name_person["name"]]

    return result
