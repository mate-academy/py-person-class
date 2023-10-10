class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)

        wife_name = person_info.get("wife")
        husband_name = person_info.get("husband")

        if wife_name is not None:
            wife = Person.people.get(wife_name)
            if wife:
                person.wife = wife
                wife.husband = person

        if husband_name is not None:
            husband = Person.people.get(husband_name)
            if husband:
                person.husband = husband
                husband.wife = person

        person_list.append(person)

    return person_list
