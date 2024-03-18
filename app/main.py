class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person_info in people:
        person = Person(person_info["name"], person_info["age"])
        if "wife" in person_info:
            wife = Person.people.get(person_info["wife"])
            if wife is not None:
                person.wife = wife
                wife.husband = person
        if "husband" in person_info:
            husband = Person.people.get(person_info["husband"])
            if husband is not None:
                person.husband = husband
                husband.wife = person
    return list(Person.people.values())
