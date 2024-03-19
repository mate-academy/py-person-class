class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)
        if "wife" in person_info and person_info["wife"] is not None:
            wife_name = person_info["wife"]
            wife_person = Person.people.get(wife_name)
            if wife_person:
                person.wife = wife_person
                wife_person.husband = person
        elif "husband" in person_info and person_info["husband"] is not None:
            husband_name = person_info["husband"]
            husband_person = Person.people.get(husband_name)
            if husband_person:
                person.husband = husband_person
                husband_person.wife = person
        person_list.append(person)
    return person_list
