class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: Person) -> list:
    person_instances = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]

        person = Person(name, age)

        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name is not None:
            person.wife = Person.people.get(wife_name)
            if person.wife:
                person.wife.husband = person  # Set the husband for the wife

        if husband_name is not None:
            person.husband = Person.people.get(husband_name)
            if person.husband:
                person.husband.wife = person  # Set the wife for the husband

        person_instances.append(person)

    return person_instances
