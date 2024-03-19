class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person_data in people:
        person_name = person_data["name"]
        new_person = Person(name=person_name, age=person_data["age"])
        result.append(new_person)

    for person_data in people:
        person_name = person_data["name"]
        person_instance = Person.people[person_name]
        if person_data.get("wife") is not None:
            person_instance.wife = Person.people[person_data["wife"]]
            person_instance.wife.husband = person_instance
        elif person_data.get("husband") is not None:
            person_instance.husband = Person.people[person_data["husband"]]
            person_instance.husband.wife = person_instance
        else:
            person_instance.wife = None
            person_instance.husband = None

    return result
