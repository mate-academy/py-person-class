class Person:

    people = {}

    def __init__(self,
                 name: str,
                 age: int,
                 ) -> None:
        self.name = name
        self.age = age

    def add_attribute(self, attribute: str, value: object) -> None:
        setattr(self, attribute, value)


def create_person_list(people: list) -> list:
    result_people_list = []
    for person in people:
        if "wife" in person:
            if person["wife"] is not None:
                for person_inner in people:
                    if person_inner["name"] == person["wife"]:
                        wife = Person(person_inner["name"],
                                      person_inner["age"])
                        result_person = Person(person["name"], person["age"])
                        result_person.add_attribute("wife", wife)
                        wife.add_attribute("husband", result_person)
                        result_people_list.append(result_person)
                        Person.people[result_person.name] = result_person

            if person["wife"] is None:
                result_person = Person(person["name"], person["age"])
                result_people_list.append(result_person)
                Person.people[result_person.name] = result_person

        if "husband" in person:
            if person["husband"] is None:
                result_person = Person(person["name"], person["age"])
                result_people_list.append(result_person)
                Person.people[result_person.name] = result_person

            if person["husband"] is not None:
                for person_inner in people:
                    if (person_inner["name"] == person["husband"]):
                        husband = Person(person_inner["name"],
                                         person_inner["age"])
                        result_person = Person(person["name"], person["age"])
                        result_person.add_attribute("husband", husband)
                        husband.add_attribute("wife", result_person)
                        result_people_list.append(result_person)
                        Person.people[result_person.name] = result_person

    return result_people_list
