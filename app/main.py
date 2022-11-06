class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    if len(people) == 0:
        return []
    list_of_object = []
    for dictionary in people:
        person_new = Person(name=dictionary["name"], age=dictionary["age"])
        list_of_object.append(person_new)
    for dictionary in people:
        if "wife" in dictionary.keys():
            for i in range(len(list_of_object)):
                if dictionary["wife"] == list_of_object[i].name:
                    index = people.index(dictionary)
                    list_of_object[index].wife = list_of_object[i]
        if "husband" in dictionary.keys():
            for i in range(len(list_of_object)):
                if dictionary["husband"] == list_of_object[i].name:
                    index = people.index(dictionary)
                    list_of_object[index].husband = list_of_object[i]
    return list_of_object
