class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person_dict in people:
        current_person_instance = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife", None)
        husband_name = person_dict.get("husband", None)
        if wife_name:
            wife_person_instance = Person.people[wife_name]
            current_person_instance.wife = wife_person_instance
        if husband_name:
            husband_person_instance = Person.people[husband_name]
            current_person_instance.husband = husband_person_instance
    return person_list
