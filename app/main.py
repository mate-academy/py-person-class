class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        person_instance = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            wife_name = person["wife"]
            person_instance.wife = Person.people[wife_name]
            Person.people[wife_name].husband = person_instance
        if "husband" in person and person["husband"]:
            husband_name = person["husband"]
            person_instance.husband = Person.people[husband_name]
            Person.people[husband_name].wife = person_instance

    return [Person.people[person["name"]] for person in people]
