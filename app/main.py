class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = list()

    # Create Person instances and populate the people dictionary
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])

    # Assign wife/husband relationships
    for person in people:
        current_person = Person.people[person["name"]]
        if "wife" in person:
            if person["wife"]:
                current_person.wife = Person.people[person["wife"]]
        elif "husband" in person:
            if person["husband"]:
                current_person.husband = Person.people[person["husband"]]
        person_list.append(current_person)

    return person_list


