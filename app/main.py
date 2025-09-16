class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = []
    for person in people:
        person = Person(person["name"], person["age"])
        instances.append(person)

    for person in people:
        if "wife" in person:
            key = "wife"
        else:
            key = "husband"

        spouse_name = person[key]
        if spouse_name is not None:
            main_obj = Person.people[person["name"]]
            spouse_obj = Person.people[spouse_name]
            setattr(main_obj, key, spouse_obj)

    return instances
