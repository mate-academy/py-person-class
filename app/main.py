class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    people = [Person(person_dict.get("name"),
                     person_dict.get("age"))
              for person_dict in people_data]

    for person_dict in people_data:
        if person_dict.get("wife") is not None:
            wife_name = person_dict.get("wife")

            if wife_name in Person.people:
                Person.people[person_dict["name"]].wife = \
                    Person.people[wife_name]

        if person_dict.get("husband") is not None:
            husband_name = person_dict.get("husband")

            if husband_name in Person.people:
                Person.people[person_dict["name"]].husband = \
                    Person.people[husband_name]

    return people
