class Person:
    people = {}

    def __init__(self, name: str, age: str,) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        spouse_name = person_dict.get("wife") or person_dict.get("husband")
        if spouse_name:
            if "wife" in person_dict:
                person.wife = Person.people[spouse_name]
            elif "husband" in person_dict:
                person.husband = Person.people[spouse_name]

    return list(Person.people.values())
