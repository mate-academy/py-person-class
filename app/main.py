class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_objects = {
        person["name"]: Person(person["name"], person["age"])
        for person in people
    }

    for person in people:
        spouse = person.get("wife") or person.get("husband")
        if spouse:
            person_object = people_objects[person["name"]]
            spouse_object = people_objects[spouse]
            if "wife" in person:
                person_object.wife = spouse_object
            else:
                person_object.husband = spouse_object

    return list(people_objects.values())
