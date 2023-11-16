class Person:
    people = {}

    def __init__(self, name: str, age: int) -> type:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_data["name"], person_data["age"])
                   for person_data in people]

    for person_data in people:
        person = Person.people[person_data["name"]]
        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name is not None:
            spouse = Person.people[spouse_name]
            if "wife" in person_data:
                person.wife = spouse
                spouse.husband = person
            else:
                person.husband = spouse
                spouse.wife = person

    return person_list
