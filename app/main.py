class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        result_list.append(person)

    for person_dict in people:
        name = person_dict["name"]
        person = Person.people[name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            wife = Person.people[wife_name]
            person.wife = wife

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            husband = Person.people[husband_name]
            person.husband = husband

    return result_list
