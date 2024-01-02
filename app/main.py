class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    Person.people.clear()
    for person in people_list:
        Person(person["name"], person["age"])

    for person in people_list:
        person_instance = Person.people[person["name"]]
        spouse_name = person.get("wife") or person.get("husband")

        if spouse_name is not None:
            if "wife" in person:
                person_instance.wife = Person.people[spouse_name]
            else:
                person_instance.husband = Person.people[spouse_name]

    return list(Person.people.values())
