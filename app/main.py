class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    # complete the dict for it be non empty
    list_of_instances = [Person(person["name"], person["age"])
                         for person in people]

    # run throw the list and set the "husband" and "wife"
    for person in people:
        current_name = Person.people.get(person.get("name"))
        if "wife" in person and person["wife"]:
            current_name.wife = Person.people.get(person["wife"])
        elif "husband" in person and person["husband"]:
            current_name.husband = Person.people.get(person["husband"])

    return list_of_instances
