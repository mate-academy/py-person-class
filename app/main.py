class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]
        husband_name = person_dict.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]
    return person_list
