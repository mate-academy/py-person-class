class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    Person.people = {}

    for p_dict in people_data:
        Person(p_dict["name"], p_dict["age"])

    result_list = []
    for p_dict in people_data:
        instance = Person.people[p_dict["name"]]

        if p_dict.get("wife"):
            instance.wife = Person.people[p_dict["wife"]]
        elif p_dict.get("husband"):
            instance.husband = Person.people[p_dict["husband"]]

        result_list.append(instance)

    return result_list
