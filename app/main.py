class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    temp_people = {}
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        temp_people[name] = Person(name, age)

    for person_data in people:
        name = person_data["name"]
        person = temp_people[name]
        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name is not None:
            spouse = temp_people[spouse_name]
            setattr(
                person, "wife" if "wife" in person_data else "husband", spouse
            )
        person_list.append(person)

    return person_list
