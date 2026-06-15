class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        current_name = person["name"]
        current_age = person["age"]
        new_person = Person(current_name, current_age)
        result_list.append(new_person)

    for person in people:
        name = person["name"]
        current_person_object = Person.people[name]

        wife_name = person.get("wife")
        if wife_name is not None:
            wife_object = Person.people[wife_name]
            current_person_object.wife = wife_object

        husband_name = person.get("husband")
        if husband_name is not None:
            husband_object = Person.people[husband_name]
            current_person_object.husband = husband_object

    return result_list
