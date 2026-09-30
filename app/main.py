class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        Person.people[name] = self
        self.age = age


def create_person_list(people: list) -> list:
    persons = []
    for entry in people:
        new_person = Person(entry["name"], entry["age"])
        persons.append(new_person)

    for init_person in people:

        current_name = init_person["name"]
        current_object = Person.people[current_name]

        wife_name = init_person.get("wife")
        if wife_name is not None:
            wife_object = Person.people[wife_name]
            setattr(current_object, "wife", wife_object)

        husband_name = init_person.get("husband")
        if husband_name is not None:
            husband_object = Person.people[husband_name]
            setattr(current_object, "husband", husband_object)

    return persons
