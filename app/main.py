class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)
        if person_data.get("wife"):
            wife_name = person_data["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
                Person.people[wife_name].husband = person
        if person_data.get("husband"):
            husband_name = person_data["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
                Person.people[husband_name].wife = person
    return person_list
