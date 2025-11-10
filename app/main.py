class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = []

    for person_data in people:
        person = Person(
            name=person_data["name"],
            age=person_data["age"]
        )
        person_list.append(person)

    for person_data in people:
        current_person = Person.people[person_data["name"]]

        spouse_key = None
        if "wife" in person_data:
            spouse_key = "wife"
        elif "husband" in person_data:
            spouse_key = "husband"

        if spouse_key:
            spouse_name = person_data.get(spouse_key)

            if spouse_name is not None:
                spouse_instance = Person.people.get(spouse_name)
                current_person.__dict__[spouse_key] = spouse_instance

    return person_list
