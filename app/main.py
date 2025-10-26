class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name is not None:
            # Search a wife for husband to make the pair
            wife = Person.people.get(wife_name)
            if wife:
                new_person.wife = wife
                wife.husband = new_person
        elif husband_name is not None:
            # Search a husband for wife to make the pair
            husband = Person.people.get(husband_name)
            if husband:
                new_person.husband = husband
                husband.wife = new_person

        person_list.append(new_person)

    return person_list
