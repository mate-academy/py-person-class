class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_data in person_list:

        for person_instance in people:

            if person_data.name == person_instance["name"]:
                wife = person_instance.get("wife")
                husband = person_instance.get("husband")

                if wife:
                    person_data.wife = Person.people[wife]
                elif husband:
                    person_data.husband = Person.people[husband]

    return person_list
