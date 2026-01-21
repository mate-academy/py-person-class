class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    result = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]

        new_person = Person(name, age)
        result.append(new_person)

        wife_name = person_data.get("wife")
        if wife_name:
            wife = Person.people.get(wife_name)
            if wife:
                new_person.wife = wife
                wife.husband = new_person

        husband_name = person_data.get("husband")
        if husband_name:
            husband = Person.people.get(husband_name)
            if husband:
                new_person.husband = husband
                husband.wife = new_person

    return result
