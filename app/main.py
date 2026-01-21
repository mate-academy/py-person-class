class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(list_of_dict: list) -> list:
    """
    Create Person List Function

    This function create list of instances of Person class
    """
    list_of_people = []
    for person in list_of_dict:
        new_person = Person(person["name"], person["age"])
        if person.get("wife") is not None:
            new_person.wife = person["wife"]
        if person.get("husband") is not None:
            new_person.husband = person["husband"]
        list_of_people.append(new_person)
    for married in list_of_people:
        if hasattr(married, "wife"):
            if married.wife in Person.people:
                married.wife = Person.people[married.wife]
        if hasattr(married, "husband"):
            if married.husband in Person.people:
                married.husband = Person.people[married.husband]
    return list_of_people
