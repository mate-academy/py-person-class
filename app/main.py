class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        instances.append(person)

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        spouse_name = person_dict.get("wife") or person_dict.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            setattr(person, "wife" if "wife" in
                                      person_dict else "husband", spouse)

    return instances
