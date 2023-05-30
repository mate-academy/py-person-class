class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

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

    return person_list
