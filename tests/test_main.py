class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.__class__.people[name] = self


def create_person_list(people):
    person_instances = []
    for person_dict in people:
        person_name = person_dict['name']
        person_age = person_dict['age']
        person = Person(person_name, person_age)
        person_instances.append(person)
        if 'wife' in person_dict and person_dict['wife'] is not None:
            wife_name = person_dict['wife']
            if wife_name not in Person.people:
                wife = Person(wife_name, None)
                Person.people[wife_name] = wife
            person.wife = Person.people[wife_name]
        if 'husband' in person_dict and person_dict['husband'] is not None:
            husband_name = person_dict['husband']
            if husband_name not in Person.people:
                husband = Person(husband_name, None)
                Person.people[husband_name] = husband
            person.husband = Person.people[husband_name]
    return person_instances


def test_create_person_list():
    people_list = [
        {'name': 'Bob', 'age': 35, 'wife': 'Alice'},
        {'name': 'Alice', 'age': 30, 'husband': 'Bob'},
        {'name': 'Charlie', 'age': 40, 'wife': 'Alice'},
        {'name': 'Eve', 'age': 25, 'husband': 'Charlie'}
    ]

    person_instances = create_person_list(people_list)
