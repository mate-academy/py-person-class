class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        # Create a Person instance
        person = Person(name, age)
        person_list.append(person)

    for person_dict in people:
        name = person_dict["name"]
        person_instance = Person.people[name]

        if "wife" in person_dict and person_dict["wife"]:
            person_instance.wife = Person.people[person_dict["wife"]]
        elif "husband" in person_dict and person_dict["husband"]:
            person_instance.husband = Person.people[person_dict["husband"]]

    return person_list
