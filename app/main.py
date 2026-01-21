class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    people_instances = [Person(person_data.get("name"), person_data.get("age"))
                        for person_data in people_data]

    for person_data in people_data:
        person = Person.people.get(person_data.get("name"))

        if person_data.get("wife"):
            wife = Person.people.get(person_data.get("wife"))
            if wife:
                person.wife = wife

        if person_data.get("husband"):
            husband = Person.people.get(person_data.get("husband"))
            if husband:
                person.husband = husband

    return people_instances
