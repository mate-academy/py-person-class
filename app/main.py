class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    new_list = [Person(d["name"], d["age"]) for d in people]

    for person_dict in people:
        current_name = person_dict["name"]
        current_person = Person.people[current_name]

        if person_dict.get("wife") is not None:
            spouse_name = person_dict["wife"]
            spouse_instance = Person.people[spouse_name]
            current_person.wife = spouse_instance

        if person_dict.get("husband") is not None:
            spouse_name = person_dict["husband"]
            spouse_instance = Person.people[spouse_name]
            current_person.husband = spouse_instance

    return new_list
