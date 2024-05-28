class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        name = person["name"]
        name_of_person = Person.people[name]

        spouse_name = person.get("wife") or person.get("husband")

        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if "wife" in person:
                name_of_person.wife = spouse
            elif "husband" in person:
                name_of_person.husband = spouse
    return person_list
