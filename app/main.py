class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result_list = []
    for person in people:
        obj_person = Person(person["name"], person["age"])
        if "wife" in person:
            if person["wife"] is not None:
                obj_person.wife = person["wife"]

        if "husband" in person:
            if person["husband"] is not None:
                obj_person.husband = person["husband"]
        result_list.append(obj_person)

    for person in result_list:
        wife = getattr(person, "wife", None)
        if wife is not None:
            person.wife = person.people[wife]

        husband = getattr(person, "husband", None)
        if husband is not None:
            person.husband = person.people[person.husband]
    return result_list
