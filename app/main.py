class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []

    for person in people:
        person_object = Person(person["name"], person["age"])
        people_list.append(person_object)
        spouse_name = person.get("wife") or person.get("husband")

        if spouse_name and spouse_name in Person.people:
            spouse_object = Person.people[spouse_name]
            if "wife" in person:
                person_object.wife = spouse_object
                spouse_object.husband = person_object
            else:
                person_object.husband = spouse_object
                spouse_object.wife = person_object

    return people_list
