class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_instance = Person.people[person["name"]]

        for relation in ["wife", "husband"]:
            spouse_name = person.get(relation)

            if spouse_name:
                spouse_instance = Person.people[spouse_name]
                setattr(person_instance, relation, spouse_instance)
    return instances
