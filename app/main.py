class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_info in people:
        name = person_info["name"]
        spouse_name = person_info.get("wife") or person_info.get("husband")

        if spouse_name:
            person = Person.people[name]
            spouse = Person.people[spouse_name]

            if "wife" in person_info:
                person.wife = spouse
            else:
                person.husband = spouse
            spouse.spouse = person

    return person_list
    pass
