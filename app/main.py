class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person_dic in people:
        current_person = Person.people[person_dic["name"]]
        if person_dic.get("wife") is not None:
            wife_name = person_dic["wife"]
            current_person.wife = Person.people[wife_name]

        if person_dic.get("husband") is not None:
            husband_name = person_dic["husband"]
            current_person.husband = Person.people[husband_name]
    return person_list
