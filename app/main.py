class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = []

    for person in people_list:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        person_instances.append(person_instance)

    for person in person_instances:
        for original_person in people_list:
            if original_person["name"] == person.name:
                spouse_key = "wife" if "wife" in original_person else "husband"
                spouse_name = original_person.get(spouse_key)
                if spouse_name:
                    if spouse_key == "wife":
                        person.wife = Person.people[spouse_name]
                    else:
                        person.husband = Person.people[spouse_name]

    return person_instances
