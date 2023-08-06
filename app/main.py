class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_name = person["name"]
        person_age = person["age"]
        person_list.append(Person(person_name, person_age))

    for index, person in enumerate(person_list):
        if people[index].get("wife") is not None:
            wife = [item
                    for item in person_list
                    if item.name == people[index].get("wife")][0]
            person.wife = wife
        elif people[index].get("husband") is not None:
            husband = [item
                       for item in person_list
                       if item.name == people[index].get("husband")][0]
            person.husband = husband
    return person_list
