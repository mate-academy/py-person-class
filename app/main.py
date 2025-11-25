class Person:

    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person_dict = Person(name, age)
        result.append(person_dict)

    for person_dict in people:
        name = person_dict["name"]
        person = Person.people[name]
        wife_name = person_dict.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        husband_name = person_dict.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]
    return result
