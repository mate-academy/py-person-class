class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    find_partner("husband", people)
    find_partner("wife", people)
    return person_list


def find_partner(status: str, people: list) -> None:
    for dict_person in people:
        if status in dict_person and dict_person[status] is not None:
            for name, person_link in Person.people.items():
                if dict_person[status] == name:
                    if status == "husband":
                        person_link.wife \
                            = Person.people[dict_person["name"]]
                    else:
                        person_link.husband \
                            = Person.people[dict_person["name"]]
                    break
