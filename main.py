class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # First pass: create Person instances and store them in the Person.people dictionary
    person_list = [Person(person["name"], person["age"]) for person in people]

    # Second pass: set spouse references using dict.get()
    for person in people:
        current_person = Person.people.get(person["name"])
        spouse_name = person.get("wife") or person.get("husband")

        if spouse_name:
            if "wife" in person:
                current_person.wife = Person.people.get(spouse_name)
            elif "husband" in person:
                current_person.husband = Person.people.get(spouse_name)

    return person_list
