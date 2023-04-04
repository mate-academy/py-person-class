
class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person['name']
        age = person['age']
        human = Person(name, age)
        if person.get('wife') is not None:
            wife_name = person['wife']
            wife = Person.people.get(wife_name)
            if wife is not None:
                human.wife = wife
                wife.husband = human
        elif person.get('husband') is not None:
            husband_name = person['husband']
            husband = Person.people.get(husband_name)
            if husband is not None:
                human.husband = husband
                husband.wife = human
        if human.wife is None:
            del human.wife
        if human.husband is None:
            del human.husband
        person_list.append(human)
    return person_list
