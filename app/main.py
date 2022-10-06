class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(list_of_dict: list) -> list:
    # """
    # Create Person List Function
    #
    # This function create list of instances of Person class
    # """
    list_of_people = []
    for person in list_of_dict:
        new_person = Person(person["name"], person["age"])
        if person.get("wife") is not None:
            new_person.wife = person["wife"]
        if person.get("husband") is not None:
            new_person.husband = person["husband"]
        list_of_people.append(new_person)
    for temp in list_of_people:
        if hasattr(temp, "wife"):
            if temp.wife in Person.people:
                temp.wife = Person.people[temp.wife]
        if hasattr(temp, "husband"):
            if temp.husband in Person.people:
                temp.husband = Person.people[temp.husband]
    return list_of_people
