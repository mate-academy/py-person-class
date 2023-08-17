class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"])
               for person in people]

    for person in people:
        person_name = person["name"]
        person_object = Person.people[person_name]
        if "wife" in person and person["wife"] is not None:
            person_object.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            person_object.husband = Person.people[person["husband"]]
    return persons
