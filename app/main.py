class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    for person_dict in people:
        Person(name=person_dict["name"], age=person_dict["age"])

    for person_dict in people:
        name = person_dict["name"]
        current_person = Person.people[name]

        spouse_key = "wife" if "wife" in person_dict else "husband"
        spouse_name = person_dict.get(spouse_key)

        if spouse_name is not None:
            spouse_instance = Person.people.get(spouse_name)
            setattr(current_person, spouse_key, spouse_instance)

    return [Person.people[p_dict["name"]] for p_dict in people]
