class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
        self.wife = None
        self.husband = None


def create_person_list(people: list) -> list:
    result = []
    for person_dict in people:
        person = Person(**person_dict)
        result.append(person)

    for person_dict in people:
        current_person = Person.people[person_dict["name"]]
        if "wife" in person_dict:
            wife_person = Person.people[person_dict["wife"]]
            current_person.wife = wife_person
        if "husband" in person_dict:
            husband_person = Person.people[person_dict["husband"]]
            current_person.husband = husband_person
    return result
