class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_dict in people:
        spouse_name = person_dict.get("wife") or person_dict.get("husband")
        if spouse_name:
            person = Person.people[person_dict["name"]]
            spouse = Person.people[spouse_name]
            setattr(person, "wife"
                    if person_dict.get("wife") else "husband", spouse)

    return person_list
