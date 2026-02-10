class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    instances = []
    for data in people:
        new_person = Person(data["name"], data["age"])
        instances.append(new_person)

    for data in people:
        name = data["name"]
        current_person = Person.people[name]
        spouse_key = "wife" if "wife" in data else "husband"
        spouse_name = data.get(spouse_key)

        if spouse_name is not None:
            spouse_instance = Person.people[spouse_name]
            setattr(current_person, spouse_key, spouse_instance)

    return instances
