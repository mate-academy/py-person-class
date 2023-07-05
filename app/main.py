class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        for key, value in person.items():
            if key == "wife" and value is not None:
                setattr(new_person, key, value)
            elif key == "husband" and value is not None:
                setattr(new_person, key, value)
        list_of_people.append(new_person)

    for i in range(len(list_of_people)):
        person = list_of_people[i]
        if hasattr(person, "wife"):
            wife_name = person.wife
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
        if hasattr(person, "husband"):
            husband_name = person.husband
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]

    return list_of_people
