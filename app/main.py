class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        person_instance = Person.people[person_data["name"]]
        spouse_key = (
            "wife" if person_data.get("wife") is not None else "husband"
        )
        spouse_name = person_data.get(spouse_key)

        if spouse_name is not None:
            setattr(person_instance, spouse_key, Person.people[spouse_name])

    return person_list
