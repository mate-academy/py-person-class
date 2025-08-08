class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_list = [Person(person["name"], person["age"]) for person in people]

    for person_data  in people:
        name = person_data["name"]
        if person_data .get("wife"):
            wife_name = person_data ["wife"]
            Person.people[name].wife = Person.people[wife_name]
        if person_data .get("husband"):
            husband_name = person_data ["husband"]
            Person.people[name].husband = Person.people[husband_name]

    return new_list
