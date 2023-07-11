class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons = []

    for person in people:

        new_person = Person(person["name"], person["age"])
        spouse_name = person.get("wife") or person.get("husband")

        if spouse_name:
            if spouse_name in Person.people:
                spouse = Person.people[spouse_name]
                if "wife" in person:
                    new_person.wife = spouse
                    spouse.husband = new_person

        persons.append(new_person)

    return persons
