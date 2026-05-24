class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        current_person = Person.people[person_dict["name"]]
        spouse_name = person_dict.get("wife") or person_dict.get("husband")
        if spouse_name:
            spouse = Person.people[spouse_name]
            current_person.wife = spouse
            current_person.wife.husband = current_person

    return result
