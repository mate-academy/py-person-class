class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def add_names_links(people: list) -> list[Person]:
    for item in people:
        for compere_item in people:
            compere_item_dict = compere_item.__dict__
            if item.name != compere_item.name \
                    and item.name in compere_item_dict.values():
                attr = str([x for x in compere_item_dict.keys()
                            if compere_item_dict[x] == item.name])
                setattr(compere_item, attr[2:-2],
                        Person.people.get(item.name))
    return people


def create_person_list(people: list[dict]) -> list:
    persons = []
    for person in people:
        init_name, init_age = person["name"], person["age"]
        appended_person = Person(
            init_name, init_age)
        rests = {key: value for key, value in person.items()
                 if value not in [init_name, init_age]
                 and value is not None}
        for key, value in rests.items():
            setattr(appended_person, key, value)
        persons.append(appended_person)
    persons = add_names_links(people=persons)
    return persons
