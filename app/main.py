class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    Person.people.clear()
    objs = [Person(d['name'], d['age']) for d in people_list]
    for data, obj in zip(people_list, objs):
        wife_name = data.get('wife')
        if wife_name is not None:
            obj.wife = Person.people[wife_name]
        husband_name = data.get('husband')
        if husband_name is not None:
            obj.husband = Person.people[husband_name]
    return objs
