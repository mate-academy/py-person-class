class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse := Person.people.get(spouse_name):
            person.spouse = spouse
            if "wife" in person_data:
                person.wife = spouse
                spouse.husband = person

    return list(Person.people.values())
