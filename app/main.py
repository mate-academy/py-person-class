class Person:
    people = {}  # : Dict[str, "Person"]

    def __init__(
            self,
            name: str,
            age: int,
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict[str, str]]) -> list[Person]:
    people_dict = [
        Person(person["name"], int(person["age"])) for person in people
    ]
    for person_data in people:
        name_of_person = person_data.get("name")
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")
        if wife_name:
            Person.people[name_of_person].wife = Person.people[wife_name]
        if husband_name:
            Person.people[name_of_person].husband = Person.people[husband_name]
    return people_dict
