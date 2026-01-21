class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    result = [
        Person(name=person["name"],
               age=person["age"]) for person in people]

    for person_dict in people:
        name = person_dict["name"]
        person_obj = Person.people[name]

        wife_name = person_dict.get("wife")
        if wife_name is not None:
            wife_name = person_dict["wife"]
            person_obj.wife = Person.people[wife_name]

        husband_name = person_dict.get("husband")
        if husband_name is not None:
            husband_name = person_dict["husband"]
            person_obj.husband = Person.people[husband_name]

    return result
