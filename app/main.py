class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:

        person = Person(person_data["name"], person_data["age"])

        if "wife" in person_data:
            wife_name = person_data["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
                person.wife.husband = person

        if "husband" in person_data:
            husband_name = person_data["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
                person.husband.wife = person

        person_list.append(person)

    return person_list
