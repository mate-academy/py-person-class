class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: dict) -> list:

    {Person(person["name"], person["age"]) for person in people}

    for person in people:
        current_person = Person.people[person["name"]]
        spouse_name = person.get("wife") or person.get("husband")

        if spouse_name and spouse_name in Person.people:
            spouse = Person.people[spouse_name]

            if "wife" in person:
                current_person.wife = spouse
                spouse.husband = current_person
            elif "husband" in person:
                current_person.husband = spouse
                spouse.wife = current_person

    return list(Person.people.values())
