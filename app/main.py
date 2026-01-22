class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    persons = [
        Person(name=person_dict["name"], age=person_dict["age"])
        for person_dict in people_list
    ]

    for person_dict in people_list:
        person = Person.people[person_dict["name"]]
        if spouse_name := person_dict.get("wife"):
            spouse = Person.people[spouse_name]
            person.wife = spouse
        elif spouse_name := person_dict.get("husband"):
            spouse = Person.people[spouse_name]
            person.husband = spouse

    return persons
