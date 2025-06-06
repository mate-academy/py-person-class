class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_class_dict = {}

    for person in people:
        people_class_dict[person["name"]] = Person(
            person["name"], person["age"]
        )

    for person in people:
        if person.get("wife"):
            people_class_dict[person["name"]].wife\
                = people_class_dict[person["wife"]]
        elif person.get("husband"):
            people_class_dict[person["name"]].husband \
                = people_class_dict[person["husband"]]

    return [person for person in people_class_dict.values()]
