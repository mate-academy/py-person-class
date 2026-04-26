class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = list()

    for curr_person in people:
        person_list.append(Person(curr_person["name"], curr_person["age"]))

    for curr_person in people:
        current_obj = Person.people[curr_person["name"]]

        if curr_person.get("husband") is not None:
            husband_name = curr_person.get("husband")
            current_obj.husband = Person.people[husband_name]

        elif curr_person.get("wife") is not None:
            wife_name = curr_person.get("wife")
            current_obj.wife = Person.people[wife_name]
    return person_list
