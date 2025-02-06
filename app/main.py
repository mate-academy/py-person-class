class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    Person.people.clear()
    temp_list = {}
    for person in people:
        temp_list[person["name"]] = Person(person["name"], person["age"])
    for person in people:
        person_obj = temp_list[person["name"]]
        if "wife" in person and person["wife"] in temp_list:
            person_obj.wife = temp_list[person["wife"]]
        if "husband" in person and person["husband"] in temp_list:
            person_obj.husband = temp_list[person["husband"]]
        Person.people[person_obj.name] = person_obj
    return list(temp_list.values())
