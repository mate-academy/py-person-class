class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_dict["name"], person_dict["age"])
                   for person_dict
                   in people]

    for person_dict, person in zip(people, person_list):
        wife_name = person_dict.get("wife")
        if wife_name:
            person.wife = Person.people[wife_name]
        husband_name = person_dict.get("husband")
        if husband_name:
            person.husband = Person.people[husband_name]
    return person_list
