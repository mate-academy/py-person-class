class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people_data: dict) -> list[Person]:
    person_list = []

    for person_item in people_data:
        name = person_item["name"]
        age = person_item["age"]
        person = Person(name, age)

        person_list.append(person)

    for person, person_item in zip(person_list, people_data):
        if "wife" in person_item:
            wife_name = person_item["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
                del person.husband
            else:
                del person.wife
                del person.husband

        if "husband" in person_item:
            husband_name = person_item["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
                del person.wife
            else:
                del person.wife
                del person.husband

    return person_list
