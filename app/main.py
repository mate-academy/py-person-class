class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        name = person["name"]
        age = person["age"]
        personal_data = Person(name, age)
        result.append(personal_data)

    for person in people:
        person_obj = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            partner = Person.people[person["wife"]]
            person_obj.wife = partner
        elif "husband" in person and person["husband"] is not None:
            partner = Person.people[person["husband"]]
            person_obj.husband = partner
    return result
