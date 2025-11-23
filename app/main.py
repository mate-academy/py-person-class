class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(data_list: list) -> list:
    persons = []

    for data in data_list:
        person = Person(data["name"], data["age"])
        persons.append(person)

    for data in data_list:
        name = data["name"]
        spouse_name = data.get("wife") or data.get("husband")

        if spouse_name:
            person = Person.people[name]
            spouse = Person.people[spouse_name]

            if "wife" in data:
                person.wife = spouse
            else:
                person.husband = spouse

    return persons
