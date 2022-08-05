class Person:

    people = {}

    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age

        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

        self.__class__.people[self.name] = self

    @classmethod
    def wife_husband(cls):
        for key_person in cls.people:

            if hasattr(cls.people[key_person], "husband"):
                if cls.people[key_person].husband in cls.people:
                    cls.people[key_person].husband = cls.people[cls.people[key_person].husband]
            elif hasattr(cls.people[key_person], "wife"):
                if cls.people[key_person].wife in cls.people:
                    cls.people[key_person].wife = cls.people[cls.people[key_person].wife]


def create_person_list(people: list) -> list:
    list_of_person_objects = [Person(**person_from_list) for person_from_list in people]
    Person.wife_husband()
    return list_of_person_objects
