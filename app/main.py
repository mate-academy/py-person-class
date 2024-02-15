class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(name=person["name"],
                          age=person["age"])
                   for person in people]
    for person in people:
        person_instance = person["name"]
        if wife_name := person.get("wife"):
            Person.people[person_instance].wife = Person.people.get(wife_name)
        if husband_name := person.get("husband"):
            Person.people[person_instance].husband = Person.people.get(husband_name)
    return people_list
