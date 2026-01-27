class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for person_dict in people:
        wife_name = person_dict.get("wife")
        if wife_name is not None:
            current_name = person_dict["name"]
            current_person = Person.people[current_name]
            wife_obj = Person.people[wife_name]
            current_person.wife = wife_obj

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            current_name = person_dict["name"]
            current_person = Person.people[current_name]
            husband_obj = Person.people[husband_name]
            current_person.husband = husband_obj

    return person_list
