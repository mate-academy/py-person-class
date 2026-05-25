class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for p in people:
        Person(p["name"], p["age"])

    def link_spouse(person_dict: dict) -> Person:
        person_instance = Person.people[person_dict["name"]]
        spouse_key = "wife" if person_dict.get("wife") else "husband"
        spouse_name = person_dict.get(spouse_key)

        if spouse_name:
            setattr(person_instance, spouse_key, Person.people[spouse_name])

        return person_instance

    return [link_spouse(p) for p in people]
