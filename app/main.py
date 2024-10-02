class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = []

    person_instances = [Person(person["name"],
                               person["age"]) for person in people_list]

    for person in person_instances:
        for original_person in people_list:
            if original_person["name"] == person.name:
                if spouse_name := (
                        original_person.get("wife"
                                            if "wife"
                                               in original_person
                                            else "husband")):
                    if "wife" in original_person:
                        person.wife = Person.people[spouse_name]
                    else:
                        person.husband = Person.people[spouse_name]

    return person_instances
