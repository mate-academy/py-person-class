class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_people = [Person(element["name"],
                         element["age"]) for element in people]
    for element in people:
        current_person = Person.people[element["name"]]
        wife_name = element.get("wife")
        if wife_name:
            wife_name = element["wife"]
            current_person.wife = Person.people.get(wife_name)
        husband_name = element.get("husband")
        if husband_name:
            husband_name = element["husband"]
            current_person.husband = Person.people.get(husband_name)
    return new_people
