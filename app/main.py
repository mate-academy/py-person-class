class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_objects = []
    for person in people:
        people_objects.append(
            Person(
                name=person["name"],
                age=person["age"]
            )
        )

    for dictionary_person in people:
        twosome = "wife" if "wife" in dictionary_person else "husband"
        name = dictionary_person["name"]
        name_of_pair = dictionary_person[twosome]
        if name_of_pair and "wife" in dictionary_person:
            Person.people[name].wife = Person.people[name_of_pair]
        elif name_of_pair and "husband" in dictionary_person:
            Person.people[name].husband = Person.people[name_of_pair]

    return people_objects
