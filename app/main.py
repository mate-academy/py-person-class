class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        self.add_to_people()

    def add_to_people(self) -> None:
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    people_list = []

    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)
        people_list.append(person)

    for index, person_info in enumerate(people):
        if "wife" in person_info and person_info["wife"]:
            wife_name = person_info["wife"]
            if wife_name in Person.people:
                people_list[index].wife = Person.people[wife_name]

        if "husband" in person_info and person_info["husband"]:
            husband_name = person_info["husband"]
            if husband_name in Person.people:
                people_list[index].husband = Person.people[husband_name]

    return people_list
