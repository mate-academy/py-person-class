class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        created_person = Person(person["name"],
                                person["age"])
        person_list.append(created_person)
    for person in people:
        person_index = people.index(person)
        if person.get("husband"):
            husband_name = person["husband"]
            person_list[person_index].husband = Person.people[husband_name]
        if person.get("wife"):
            wife_name = person["wife"]
            person_list[person_index].wife = Person.people[wife_name]
    return person_list
