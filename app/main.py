class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def add_attribute(self, attribute: str, value: object) -> None:
        setattr(self, attribute, value)


def create_person_list(people: list) -> list:
    result_people_list = []

    for person_dict in people:
        Person.people[person_dict["name"]] = Person(person_dict["name"],
                                                    person_dict["age"])

    for person in people:
        person_obj = Person.people.get(person["name"])

        wife = person.get("wife")
        if wife:
            wife_obj = Person.people.get(wife)
            person_obj.add_attribute("wife", wife_obj)
            wife_obj.add_attribute("husband", person_obj)

        result_people_list.append(person_obj)

    return result_people_list
