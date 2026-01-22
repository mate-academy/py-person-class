class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    Person.people.clear()

    person_list = []
    for person in people:
        person_obj = Person(person["name"], person["age"])

        if "wife" in person and person["wife"] is not None:
            person_obj._wife_name = person["wife"]
        if "husband" in person and person["husband"] is not None:
            person_obj._husband_name = person["husband"]

        person_list.append(person_obj)

    for person in person_list:
        if hasattr(person, "_wife_name"):
            wife_obj = Person.people.get(person._wife_name)
            if wife_obj:
                person.wife = wife_obj
            del person._wife_name
        if hasattr(person, "_husband_name"):
            husband_obj = Person.people.get(person._husband_name)
            if husband_obj:
                person.husband = husband_obj
            del person._husband_name

    return person_list
