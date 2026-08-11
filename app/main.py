class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        temp_inst = Person.people[person["name"]]
        if person.get("wife") is not None:
            temp_inst.wife = Person.people.get(person["wife"])

        if person.get("husband") is not None:
            temp_inst.husband = Person.people.get(person["husband"])

    return result
