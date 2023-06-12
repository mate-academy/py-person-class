class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self

    @classmethod
    def finding_a_spouse(cls, registry_office_list: list[dict]) -> None:
        for one_of_people in registry_office_list:
            if ("wife" in one_of_people.keys()
                    and one_of_people["wife"] is not None):
                if one_of_people["name"] in Person.people.keys():
                    Person.people[
                        one_of_people["name"]
                    ].wife = Person.people[one_of_people["wife"]]

            if ("husband" in one_of_people.keys()
                    and one_of_people["husband"] is not None):
                if one_of_people["name"] in Person.people.keys():
                    Person.people[
                        one_of_people["name"]
                    ].husband = Person.people[one_of_people["husband"]]


def create_person_list(people: list) -> list:
    for one_of_people in people:
        Person(one_of_people["name"], one_of_people["age"])

    Person.finding_a_spouse(people)

    return [Person.people[one_result] for one_result in Person.people]
