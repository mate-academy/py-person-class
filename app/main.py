class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def link_spouses(person_instance: Person, person_data: dict) -> None:
    spouse_key = "wife" if "wife" in person_data else "husband"
    spouse_name = person_data.get(spouse_key)

    if spouse_name:
        spouse_instance = Person.people.get(spouse_name)
        if spouse_instance:
            setattr(person_instance, spouse_key, spouse_instance)
            setattr(
                spouse_instance,
                "husband" if spouse_key == "wife"
                else "wife",
                person_instance
            )


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    for person_data in people:
        person_instance = Person(person_data["name"], person_data["age"])
        link_spouses(person_instance, person_data)
        person_list.append(person_instance)

    return person_list
