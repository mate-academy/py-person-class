class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    list_of_objects = [Person(name=p["name"], age=p["age"]) for p in people]

    for dict_people in people:
        current_people = Person.people[dict_people["name"]]
        if dict_people.get("wife"):
            wife_name = dict_people["wife"]
            current_people.wife = Person.people[wife_name]

        if dict_people.get("husband"):
            husband_name = dict_people["husband"]
            current_people.husband = Person.people[husband_name]

    return list_of_objects
