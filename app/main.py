class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        self.change_people(self)

    @classmethod
    def change_people(cls, self: object) -> None:
        cls.people[self.name] = self

    @classmethod
    def finding_a_spouse(cls, registry_office_list: list) -> None:
        for one_of_people in registry_office_list:
            if "wife" in one_of_people.keys():
                for find_person in Person.people:
                    if one_of_people["wife"] == find_person:
                        Person.people[one_of_people["name"]].wife = \
                            Person.people[find_person]
            if "husband" in one_of_people.keys():
                for find_person in Person.people:
                    if one_of_people["husband"] == find_person:
                        Person.people[one_of_people["name"]].husband = \
                            Person.people[find_person]


def create_person_list(people: list) -> list:
    for one_of_people in people:
        Person(one_of_people["name"], one_of_people["age"])

    Person.finding_a_spouse(people)

    return [Person.people[one_result] for one_result in Person.people]
