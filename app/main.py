class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_completed_people = [Person(i["name"], i["age"]) for i in people]

    for index, person in enumerate(people):
        try:
            wife = Person.people[person["wife"]]
            list_of_completed_people[index].wife = wife
        except KeyError:
            try:
                husband = Person.people[person["husband"]]
                list_of_completed_people[index].husband = husband
            except KeyError:
                pass

    return list_of_completed_people
