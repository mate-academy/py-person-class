class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_object = Person.people.get(name) or Person(name, age)

        wife_name = person.get("wife")
        if wife_name is not None:
            wife = Person.people.get(wife_name) or Person(wife_name, None)
            person_object.wife = wife

        husband_name = person.get("husband")
        if husband_name is not None:
            husband = Person.people.get(husband_name) or Person(
                husband_name, None)
            person_object.husband = husband

        person_list.append(person_object)
    return person_list
