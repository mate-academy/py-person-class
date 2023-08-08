class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances_list = []

    for person_dict in people:
        person_instance = Person(person_dict["name"], person_dict["age"])
        person_instances_list.append(person_instance)

    for person_dict in people:
        name = person_dict["name"]
        marriage_name = person_dict.get("wife") or person_dict.get("husband")

        if marriage_name:
            person_instance = Person.people[name]
            marriage_couple_instance = Person.people[marriage_name]

            if "wife" in person_dict:
                person_instance.wife = marriage_couple_instance
            else:
                person_instance.husband = marriage_couple_instance

    return person_instances_list
