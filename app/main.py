class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]

        person_instance = Person(name, age)

        wife_name = person_data.get("wife")
        if wife_name is not None:
            person_instance.wife = Person.people.get(wife_name)
            if person_instance.wife:
                person_instance.wife.husband = person_instance

        husband_name = person_data.get("husband")
        if husband_name is not None:
            person_instance.husband = Person.people.get(husband_name)
            if person_instance.husband:
                person_instance.husband.wife = person_instance

        person_instances.append(person_instance)

    return person_instances
