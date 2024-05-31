class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_data in people:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            person.wife = Person.people[wife_name]
            Person.people[wife_name].husband = person
        elif "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            person.husband = Person.people[husband_name]
            Person.people[husband_name].wife = person
        elif hasattr(person, "wife"):
            delattr(person, "wife")
        elif hasattr(person, "husband"):
            delattr(person, "husband")

    return person_list
