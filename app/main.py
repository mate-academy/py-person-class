class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people: list) -> list:
    Person.people = {}

    [Person(person_dict["name"], person_dict["age"]) for person_dict in people]
    for person_dict in people:
        p = Person.people[person_dict["name"]]

        wife_name = person_dict["wife_name"]
        if wife_name:
            p.wife = Person.people[wife_name]

        husband_name = person_dict["husband_name"]
        if husband_name:
            p.husband = Person.people[husband_name]

    return list(Person.people.values())

