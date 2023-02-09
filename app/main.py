class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list[dict[str, ]]) -> None:
    person_list = []
    for item in people_dicts:
        person = Person(item["name"], item["age"])
        if "wife" in item.keys():
            if item["wife"]:
                person.wife = item["wife"]
        elif "husband" in item.keys():
            if item["husband"]:
                person.husband = item["husband"]
        person_list.append(person)

    for person in person_list:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return person_list
