class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None

        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]

        person = Person(name, age)
        person_list.append(person)

    for person_dict in people:
        name = person_dict["name"]
        spouse_name = person_dict.get("wife") or person_dict.get("husband")

        if spouse_name:
            person = Person.people[name]
            spouse = Person.people.get(spouse_name)
            if spouse:
                person.spouse = spouse
                setattr(person, "wife" if "wife" in
                                          person_dict else "husband", spouse)
    return person_list
