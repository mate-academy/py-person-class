class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    for p_dict in people:
        Person(p_dict["name"], p_dict["age"])

    result = []
    for p_dict in people:
        name = p_dict["name"]
        current_person = Person.people[name]

        if "wife" in p_dict and p_dict["wife"] is not None:
            spouse_name = p_dict["wife"]
            current_person.wife = Person.people[spouse_name]
        elif "husband" in p_dict and p_dict["husband"] is not None:
            spouse_name = p_dict["husband"]
            current_person.husband = Person.people[spouse_name]

        result.append(current_person)

    return result
