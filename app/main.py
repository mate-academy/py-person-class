class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    person_instances = []
    for person_dict in people:
        name = person_dict["name"]
        person_instance = Person.people[name]

        spouse_key = "wife" if person_dict.get("wife") else "husband"
        spouse_name = person_dict.get(spouse_key)

        if spouse_name is not None:
            setattr(person_instance, spouse_key, Person.people[spouse_name])

        person_instances.append(person_instance)

    return person_instances
