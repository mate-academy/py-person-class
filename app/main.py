class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    new_people_list = []
    for person in people:
        new_people_list.append(Person(person["name"], person["age"]))
    for new_people in new_people_list:
        for index, dict_person in enumerate(people):
            if "wife" in dict_person:
                if dict_person["wife"] == new_people.name:
                    new_people_list[index].wife = new_people
                    new_people.husband = new_people_list[index]
    return new_people_list
