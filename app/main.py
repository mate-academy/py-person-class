class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: dict) -> list:

    for person_info in people:
        Person(person_info["name"], person_info["age"])

    for person_info in people:
        person = Person.people[person_info["name"]]
        if person_info.get("wife"):
            wife_name = person_info["wife"]
            person.wife = Person.people[wife_name]
            Person.people[wife_name].husband = person
        elif "husband" in person_info and person_info["husband"] is not None:
            husband_name = person_info["husband"]
            person.husband = Person.people[husband_name]
            Person.people[husband_name].wife = person

    return list(Person.people.values())
