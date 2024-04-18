class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person_list.append(Person(name, age))

    for person_data in people:
        if "wife" in person_data:
            current_person = None
            spouse_person = None
            for person in person_list:
                if person_data["name"] == person.name:
                    current_person = person
                if person_data["wife"] == person.name:
                    spouse_person = person
            if current_person is not None and spouse_person is not None:
                current_person.wife = spouse_person
        elif "husband" in person_data:
            current_person = None
            spouse_person = None
            for person in person_list:
                if person_data["name"] == person.name:
                    current_person = person
                if person_data["husband"] == person.name:
                    spouse_person = person
            if current_person is not None and spouse_person is not None:
                current_person.husband = spouse_person
    return person_list
