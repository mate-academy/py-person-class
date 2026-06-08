class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        wife_name = person_dict.get("wife")
        if wife_name is not None:
            wife = Person.people[wife_name]
            person.wife = wife

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            husband = Person.people[husband_name]
            person.husband = husband

    return [Person.people[person_dict["name"]] for person_dict in people]
