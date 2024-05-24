class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        person_list.append(person_instance)
    for person in people:
        name = person["name"]
        person_instance = Person.people[name]
        if "wife" in person and person["wife"]:
            wife_instance = Person.people[person["wife"]]
            person_instance.wife = wife_instance
            wife_instance.husband = person_instance
        elif "husband" in person and person["husband"]:
            husband_instance = Person.people[person["husband"]]
            person_instance.husband = husband_instance
            husband_instance.wife = person_instance

    return person_list
