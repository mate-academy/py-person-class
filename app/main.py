class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person in people:
        current_person = Person(person["name"], person["age"])
        if person.get("wife"):
            wife_name = person["wife"]
            if wife_name in Person.people:
                wife = Person.people[wife_name]
                current_person.wife = wife
                wife.husband = current_person
        if person.get("husband"):
            husband_name = person["husband"]
            if husband_name in Person.people:
                husband = Person.people[husband_name]
                current_person.husband = husband
                husband.wife = current_person
        person_instances.append(current_person)
    return person_instances
