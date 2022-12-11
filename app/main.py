class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        persons_list.append(person)

    for person_dict in people:
        current_person = persons_list[
            [x.name for x in persons_list].index(person_dict["name"])]
        if "husband" in person_dict.keys() \
                and person_dict["husband"] is not None:
            current_person.husband = persons_list[
                [x.name for x in persons_list].index(person_dict["husband"])]
        elif "wife" in person_dict.keys() \
                and person_dict["wife"] is not None:
            current_person.wife = persons_list[
                [x.name for x in persons_list].index(person_dict["wife"])]
    return persons_list
