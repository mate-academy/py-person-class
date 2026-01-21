class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people_list: list) -> list:
    persons = []

    for person_dict in people_list:
        person = Person(person_dict["name"], person_dict["age"])
        persons.append(person)

    for person_dict in people_list:
        if "wife" in person_dict and person_dict["wife"] is not None:
            setattr(Person.people[person_dict.get("name")],
                    "wife", Person.people[person_dict.get("wife")])

        if "husband" in person_dict and person_dict["husband"] is not None:
            setattr(Person.people[person_dict["name"]],
                    "husband", Person.people[person_dict["husband"]])

    return persons
