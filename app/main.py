class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_info in people:
        person = Person(person_info["name"], person_info["age"])
        person_instances.append(person)

    for person_info in people:
        person = Person.people[person_info["name"]]
        spouse_key = "wife" if "wife" in person_info else "husband"
        spouse_name = person_info.get(spouse_key)
        if spouse_name:
            setattr(person, spouse_key, Person.people[spouse_name])

    return person_instances
