class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person in people:
        person_instance = Person(person["name"], person["age"])
        person_instances.append(person_instance)

    for person in people:
        person_obj = Person.people[person["name"]]
        husband_name = person.get("husband")
        wife_nam = person.get("wife")
        if husband_name:
            person_obj.husband = Person.people.get(husband_name)
        if wife_nam:
            person_obj.wife = Person.people.get(wife_nam)

    return person_instances
