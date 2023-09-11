class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people_list: list) -> list:
    person_list = []

    for person_dict in people_list:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)

        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name:
            person.wife = Person.people.get(wife_name)
            if person.wife:
                person.wife.husband = person

        if husband_name:
            person.husband = Person.people.get(husband_name)
            if person.husband:
                person.husband.wife = person

        person_list.append(person)
        Person.people[name] = person

    return person_list
