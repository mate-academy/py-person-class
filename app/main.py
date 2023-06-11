class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    for one_of_people in people:
        Person.people[one_of_people["name"]] = \
            Person(one_of_people["name"], one_of_people["age"])

    for one_of_people in people:
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

    result_people = []
    for one_result in Person.people:
        result_people.append(Person.people[one_result])

    return result_people
