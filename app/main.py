class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    list_of_objects = []
    for dict_people in people:
        new_item = Person(name=dict_people["name"], age=dict_people["age"])
        list_of_objects.append(new_item)

    for dict_people in people:
        current_people = Person.people[dict_people["name"]]
        if "wife" in dict_people and dict_people["wife"] is not None:
            wife_name = dict_people["wife"]
            current_people.wife = Person.people[wife_name]

        if "husband" in dict_people and dict_people["husband"] is not None:
            husband_name = dict_people["husband"]
            current_people.husband = Person.people[husband_name]

    return list_of_objects
