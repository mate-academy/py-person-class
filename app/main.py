class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_person_in_the_dict(self)

    @classmethod
    # В даному випадку, я написав анотацію any до person,
    # тому що не проходив тест -
    # test_person_instance_attribute_wife_and_husband_doesnt_exists
    def add_person_in_the_dict(cls, person: any) -> None:
        cls.people[person.name] = person


def create_person_list(persons: list) -> list:
    list_of_people = []
    for person in persons:
        new_person = Person(person["name"], person["age"])

        if person.get("wife"):
            new_person.wife = person["wife"]
        elif person.get("husband"):
            new_person.husband = person["husband"]

        list_of_people.append(new_person)

    for dude in list_of_people:
        if "wife" in dude.__dict__:
            name = dude.wife
            dude.wife = Person.people[name]
        elif "husband" in dude.__dict__:
            name = dude.husband
            dude.husband = Person.people[name]

    return list_of_people
