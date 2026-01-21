class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    final_list = []

    for person in people:
        name = person["name"]
        age = person["age"]
        wife_name = person.get("wife")
        husband_name = person.get("husband")

        new_person = Person(name, age)

        if wife_name:
            wife = Person.people.get(wife_name)
            if wife:
                new_person.wife = wife
                wife.husband = new_person

        if husband_name:
            husband = Person.people.get(husband_name)
            if husband:
                new_person.husband = husband
                husband.wife = new_person

        final_list.append(new_person)

    return final_list
