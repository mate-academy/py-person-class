class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(person_list: list) -> list:
    result_list = [Person(name=person["name"], age=person["age"])
                   for person in person_list]
    for index, person in enumerate(result_list):
        person_data = person_list[index]
        if person_data.get("wife") is not None:
            wife = find_person_by_name(person_data.get("wife"), result_list)
            person.wife = wife
            wife.husband = person
        elif person_data.get("husband") is not None:
            husband_data = person_data.get("husband")
            husband = find_person_by_name(husband_data, result_list)
            person.husband = husband
            husband.wife = person
    return result_list


def find_person_by_name(name: str, person_list: list) -> Person:
    for person in person_list:
        if person.name == name:
            return person
