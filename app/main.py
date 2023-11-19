class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person in people:
        person_list = Person(person["name"], person["age"])
        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            if wife_name in Person.people:
                person_list.wife = Person.people[wife_name]
                Person.people[wife_name].husband = person_list

        elif "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            if husband_name in Person.people:
                person_list.husband = Person.people[husband_name]
                Person.people[husband_name].wife = person_list

        person_instances.append(person_list)
    return person_instances
