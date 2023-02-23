class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    links_of_instances = []
    for person in people:
        person_obj = Person(
            person["name"],
            person["age"],
        )

        if person.get("wife"):
            wife = Person.people.get(person.get("wife"))

            if wife:
                person_obj.wife = wife
                wife.husband = person_obj
        elif person.get("husband"):
            husband = Person.people.get(person.get("husband"))

            if husband:
                person_obj.husband = husband
                husband.wife = person_obj

        links_of_instances.append(person_obj)

    return links_of_instances
