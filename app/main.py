class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    Person.people = {}

    persons = [Person(p["name"], p["age"]) for p in people_data]

    for person_dict in people_data:
        person = Person.people[person_dict["name"]]

        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name is not None:
            setattr(person, "wife", Person.people[wife_name])

        if husband_name is not None:
            setattr(person, "husband", Person.people[husband_name])

    return persons
