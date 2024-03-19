class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_person = []
    for person in people:
        person_name = person.get("name")
        person_age = person.get("age")
        person = Person(person_name, person_age)
        list_of_person.append(person)
    for person in people:
        person_name = person.get("name")
        if "wife" in person:
            wife_name = person.get("wife")
            if wife_name in Person.people:
                Person.people[person_name].wife = (
                    Person.people[wife_name]
                )
        elif "husband" in person:
            husband_name = person.get("husband")
            if husband_name in Person.people:
                Person.people[person_name].husband = (
                    Person.people[husband_name]
                )
    return list_of_person
