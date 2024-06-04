class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:

        if list(person.values())[2]:
            if list(person.keys())[2] == "wife":
                person_list.append(Person(person["name"], person["age"]))
                if person["wife"] in person_list[-1].people:
                    person_list[-1].wife \
                        = person_list[-1].people[person["wife"]]
                    person_list[-1].people[person["wife"]].husband \
                        = person_list[-1]
                else:
                    person_list[-1].wife = None
            else:
                person_list.append(Person(person["name"], person["age"]))
                if person["husband"] in person_list[-1].people:
                    person_list[-1].husband \
                        = person_list[-1].people[person["husband"]]
                    person_list[-1].people[person["husband"]].wife \
                        = person_list[-1]
                else:
                    person_list[-1].husband = None
        else:
            person_list.append(Person(person["name"], person["age"]))

    return person_list
