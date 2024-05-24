class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        name = person["name"]
        person_instance = Person.people[name]

        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name is not None:
            wife_instance = Person.people.get(wife_name)
            if wife_instance:
                person_instance.wife = wife_instance
                wife_instance.husband = person_instance
        else:
            if hasattr(person_instance, "wife"):
                del person_instance.wife

        if husband_name is not None:
            husband_instance = Person.people.get(husband_name)
            if husband_instance:
                person_instance.husband = husband_instance
                husband_instance.wife = person_instance
        else:
            if hasattr(person_instance, "husband"):
                del person_instance.husband

    return person_list
