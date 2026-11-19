class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result_list = [Person(person["name"], person["age"]) for person in people]
    for person_dict, person in zip(people, result_list):
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = person_dict["wife"]
        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = person_dict["husband"]

    for person in result_list:
        wife = getattr(person, "wife", None)
        if wife is not None:
            person.wife = person.people[wife]
        husband = getattr(person, "husband", None)
        if husband is not None:
            person.husband = person.people[person.husband]
    return result_list
