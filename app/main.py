class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: dict) -> list:
    person_list = []
    for person_data in people:
        Person(person_data["name"], person_data["age"])

    for char in people:
        wife_name = char.get("wife")
        husband_name = char.get("husband")

        instance = Person.people.get(char["name"])

        if wife_name:
            instance.wife = Person.people.get(wife_name)
        elif husband_name:
            instance.husband = Person.people.get(husband_name)
        person_list.append(instance)
    return person_list
