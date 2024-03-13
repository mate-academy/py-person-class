class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    p_list = []

    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        p_list.append(person)

    for person_data, person in zip(people, p_list):
        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            wife = next((p for p in p_list if p.name == wife_name), None)
            if wife:
                person.wife = wife
        elif "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            husband = next((p for p in p_list if p.name == husband_name), None)
            if husband:
                person.husband = husband

    return p_list
