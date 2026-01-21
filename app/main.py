class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_dict["name"], person_dict["age"]) for
                   person_dict in people]

    for person_dict in people:
        current_person_instance = Person.people[person_dict["name"]]

        wife_name = person_dict.get("wife", None)
        if wife_name:
            wife_person_instance = Person.people[wife_name]
            current_person_instance.wife = wife_person_instance
            wife_person_instance.husband = current_person_instance

        husband_name = person_dict.get("husband", None)
        if husband_name:
            husband_person_instance = Person.people[husband_name]
            current_person_instance.husband = husband_person_instance
            husband_person_instance.wife = current_person_instance

    return person_list
