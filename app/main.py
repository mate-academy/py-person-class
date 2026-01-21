class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(data["name"], data["age"]) for data in people]

    for data in people:
        person = Person.people[data["name"]]
        spouse_name = data.get("wife") or data.get("husband")

        if spouse_name is not None and spouse_name in Person.people:
            spouse = Person.people[spouse_name]
            if "wife" in data and spouse_name:
                person.wife = spouse
                spouse.husband = person
            elif "husband" in data and spouse_name:
                person.husband = spouse
                spouse.wife = person

    for person in persons:
        if person.wife is None:
            del person.wife
        if person.husband is None:
            del person.husband

    return persons
