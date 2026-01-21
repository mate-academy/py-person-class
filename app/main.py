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
        relationship_keys = ["wife", "husband"]
        for relationship in relationship_keys:
            if (relationship in person_info
                    and person_info[relationship] is not None):
                related_person = Person.people.get(person_info[relationship])
                if related_person:
                    setattr(person, relationship, related_person)
                    setattr(related_person,
                            "husband" if relationship == "wife" else "wife"
                            , person)
        person_list.append(person)
    return person_list
