class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Creating all Person instances
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])

    # Seting the wife/husband attributes
    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]
        if person_dict.get("wife", None):
            person_instance.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband", None):
            person_instance.husband = Person.people[person_dict["husband"]]

    # Returning the list of Person instances
    return list(Person.people.values())
