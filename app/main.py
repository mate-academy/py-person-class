class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people_list: list[dict]) -> list[Person]:

    person_list = []
    for pers in people_list:
        name = pers["name"]
        age = pers["age"]
        new_person = Person(name, age)
        person_list.append(new_person)
    for pers in people_list:
        wife_name, husband_name = pers.get("wife"), pers.get("husband")
        if wife_name:
            Person.people.get(pers["name"]).wife = Person.people.get(wife_name)

        if husband_name:
            Person.people.get(pers["name"]).husband = \
                Person.people.get(husband_name)

    return person_list
