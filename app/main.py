class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # self.spouse = None
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_info in people:
        person = Person(person_info["name"], person_info["age"])
        if person_info.get("wife") in Person.people:
            spouse_name = person_info.get("wife")
            person.wife = Person.people[spouse_name]
            Person.people[spouse_name].husband = person
        elif person_info.get("husband") in Person.people:
            spouse_name = person_info.get("husband")
            person.husband = Person.people[spouse_name]
            Person.people[spouse_name].wife = person
        person_instances.append(person)
    return person_instances
