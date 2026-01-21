class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    object_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_obj = Person.people[person["name"]]

        if wife_name := person.get("wife"):
            person_obj.wife = Person.people.get(wife_name)

        if husband_name := person.get("husband"):
            person_obj.husband = Person.people.get(husband_name)

    return object_list
