class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    pass


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    Person.people = {person.name: person for person in person_list}

    for i in range(len(person_list)):

        if list(people[i].values())[2] is not None:
            for person in person_list:
                if people[i][list(people[i].keys())[2]] == person.name:

                    if list(people[i].keys())[2] == "wife":
                        person_list[i].wife = person
                    else:
                        person_list[i].husband = person

                    break

    return person_list
