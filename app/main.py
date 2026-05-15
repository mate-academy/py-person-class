class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for i in range(len(people)):
        person_dict = people[i]
        person_obj = person_list[i]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            setattr(person_obj, "wife", Person.people[wife_name])

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            setattr(person_obj, "husband", Person.people[husband_name])
    return person_list
