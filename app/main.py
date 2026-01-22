class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(human["name"], human["age"]) for human in people]

    for person_dict in people:
        wife_name = person_dict.get("wife")
        if wife_name:
            Person.people[person_dict["name"]].wife = Person.people[
                person_dict["wife"]]

        husband_name = person_dict.get("husband")
        if husband_name:
            Person.people[person_dict["name"]].husband = Person.people[
                person_dict["husband"]]

    return person_list
