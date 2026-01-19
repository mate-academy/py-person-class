class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # add instance to the dict as name : instance
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    result_list = []
    # iterate over input list of dicts and create Person objects first
    for element in people:
        # temp values for future obj initialization
        name = element["name"]
        age = element["age"]
        # obj initialisation now
        result_list.append(Person(name, age))
    # iterate over people list a second time,
    # now adding referenes to object instances for relatives
    for element in people:
        # temp object to work with
        obj = Person.people[element["name"]]
        # check if dict has "wife"/"husband" keys
        # add instance references if it does
        if element.get("wife"):
            obj.wife = Person.people[element["wife"]]
        elif element.get("husband"):
            obj.husband = Person.people[element["husband"]]

    return result_list
