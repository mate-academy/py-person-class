class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_objects = {}
    person_list = []

    # Create people first
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        new_person = Person(name, age)
        person_objects[name] = new_person
        person_list.append(new_person)

    # Establish relationships after creating all people
    for person_data in people:
        name = person_data["name"]
        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            if wife_name in person_objects:
                person_objects[name].wife = person_objects[wife_name]
                person_objects[wife_name].husband = person_objects[name]
        elif "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            if husband_name in person_objects:
                person_objects[name].husband = person_objects[husband_name]
                person_objects[husband_name].wife = person_objects[name]
    return person_list
