
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    my_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person_instance = Person(name, age)
        my_list.append(person_instance)

    for person_data in people:
        current_person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            if wife_name in Person.people:
                current_person.wife = Person.people[wife_name]

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            if husband_name in Person.people:
                current_person.husband = Person.people[husband_name]

    return my_list
