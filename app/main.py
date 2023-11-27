class Person:
    people = {}

    def __init__(self, name: str, age: int, *args) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = []
    for people in people_list:
        person_instance = Person(people["name"], people["age"])
        if people.get("wife") is not None:
            person_instance.wife = Person.people.get(people["wife"])
            if person_instance.wife is not None:
                person_instance.wife.husband = person_instance

        elif people.get("husband") is not None:
            person_instance.husband = Person.people.get(people["husband"])
            if person_instance.husband is not None:
                person_instance.husband.wife = person_instance

        person_instances.append(person_instance)

    return person_instances
