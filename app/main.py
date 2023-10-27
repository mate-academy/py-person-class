class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    married_dict = {}
    result = []

    for item in people:
        person = Person(name=item["name"], age=item["age"])
        married_dict[item["name"]] = person
        result.append(person)

    for item in people:
        person_obj = married_dict[item["name"]]
        if item.get("wife") is not None:
            person_obj.wife = married_dict[item["wife"]]
        elif item.get("husband") is not None:
            person_obj.husband = married_dict[item["husband"]]

    return result
