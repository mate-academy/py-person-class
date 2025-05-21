class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []

    for human_dict in people:
        Person(human_dict["name"], human_dict["age"])

    for human_dict in people:
        current_person = Person.people[human_dict["name"]]
        if "wife" in human_dict and human_dict["wife"]:
            current_person.wife = Person.people[human_dict["wife"]]
        elif "husband" in human_dict and human_dict["husband"]:
            current_person.husband = Person.people[human_dict["husband"]]

    for human_dict in people:
        result_list.append(Person.people[human_dict["name"]])

    return result_list
