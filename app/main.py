class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        instance = Person(person["name"], person["age"])
        for person_info in person:
            if person[person_info] is not None \
                    and (person_info == "wife" or person_info == "husband"):
                setattr(instance, person_info, person[person_info])
        result.append(instance)

    for instance_person in result:
        if hasattr(instance_person, "wife"):
            instance_person.wife = Person.people[instance_person.wife]
        elif hasattr(instance_person, "husband"):
            instance_person.husband = Person.people[instance_person.husband]

    return result
