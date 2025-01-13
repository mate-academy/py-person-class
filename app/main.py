class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people) -> list:
    person_list = []

    for person in people:
        p = Person(person["name"], person["age"])

        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            if wife_name in Person.people:
                p.wife = Person.people[wife_name]
                p.wife.husband = p

        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            if husband_name in Person.people:
                p.husband = Person.people[husband_name]
                p.husband.wife = p

        person_list.append(p)

    return person_list
