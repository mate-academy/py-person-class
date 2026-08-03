class Person:
    people: dict[str, Person] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_dict: dict[str, Person] = {
        person["name"]: Person(person["name"], person["age"])
        for person in people
    }
    for person in people:

        wife = person.get("wife")
        if wife and wife in person_dict:
            person_dict[person["name"]].wife = person_dict[wife]
            person_dict[wife].husband = person_dict[person["name"]]

    return list(person_dict.values())
