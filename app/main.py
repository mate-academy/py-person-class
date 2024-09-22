class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    # Creating people without relationship
    person_list = [Person(person_dict["name"], person_dict["age"])
                   for person_dict in people]

    # Adding references to wives/husbands
    for person_dict in people:
        name = person_dict["name"]
        current_person = Person.people[name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            current_person.wife = Person.people[wife_name]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            current_person.husband = Person.people[husband_name]

    return person_list
