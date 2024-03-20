class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_info in people:
        person = Person(person_info["name"], person_info["age"])
        if "wife" in person_info and person_info["wife"] is not None:
            wife_person = Person.people.get(person_info["wife"])
            if wife_person:
                person.wife = wife_person
                wife_person.husband = person

        elif "husband" in person_info and person_info["husband"] is not None:
            husband_person = Person.people.get(person_info["husband"])
            if husband_person:
                person.husband = husband_person
                husband_person.wife = person
        person_list.append(person)
    return person_list
