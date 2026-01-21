class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]

        person_instance = Person(name, age)
        person_list.append(person_instance)

    for person_data in people:
        name = person_data["name"]
        spouse_name = person_data.get("wife") or person_data.get("husband")

        if spouse_name is not None:
            person_instance = Person.people[name]
            spouse_instance = Person.people[spouse_name]
            setattr(person_instance, "wife" if "wife"
                    in person_data else "husband", spouse_instance)
            person_instance.spouse = spouse_instance
            spouse_instance.spouse = person_instance

    return person_list
