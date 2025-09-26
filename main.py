class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        current = Person.people.get(person["name"])
        spouse_name = person.get("wife") or person.get("husband")

        if spouse_name:
            if "wife" in person:
                current.wife = Person.people.get(spouse_name)
            elif "husband" in person:
                current.husband = Person.people.get(spouse_name)

    return person_list
