class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: Person) -> list:
    person_instances = [
        Person(
            person_data["name"],
            person_data["age"]
        ) for person_data in people
    ]

    for person_data, person_instance in zip(people, person_instances):
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name and wife_name is not None:
            person_instance.wife = Person.people.get(wife_name)
            if person_instance.wife:
                person_instance.wife.husband = person_instance

        if husband_name and husband_name is not None:
            person_instance.husband = Person.people.get(husband_name)
            if person_instance.husband:
                person_instance.husband.wife = person_instance

    return person_instances
