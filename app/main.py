class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: dict) -> list:
    person_list = [
        Person(person_info["name"], person_info["age"])
        for person_info in people
    ]
    Person.people = {person.name: person for person in person_list}

    for person_info in people:
        name = person_info["name"]
        if person_info.get("wife"):
            wife_name = person_info.get("wife")
            person_instance = Person.people[name]
            spouse_instance = Person.people[wife_name]
            person_instance.wife = spouse_instance
            spouse_instance.husband = person_instance
        elif person_info.get("husband"):
            husband_name = person_info.get("husband")
            person_instance = Person.people[name]
            spouse_instance = Person.people[husband_name]
            person_instance.husband = spouse_instance
            spouse_instance.wife = person_instance

    return person_list
