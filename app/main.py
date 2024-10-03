class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_person = []
    for person_data in people:
        person_object = Person(person_data["name"], person_data["age"])
        list_of_person.append(person_object)

    for person_data in people:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data and person_data["husband"]:
            person.husband = Person.people[person_data["husband"]]

    return list_of_person
