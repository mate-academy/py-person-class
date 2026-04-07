class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        obj = Person(person["name"], person["age"])
        person_list.append(obj)
    for person in people:
        obj = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            obj.wife = Person.people[wife_name]

        elif "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            obj.husband = Person.people[husband_name]
    return person_list
