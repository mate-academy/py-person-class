class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    people_instance_list = []
    for person in people:
        people_instance_list.append(Person(person["name"], person["age"]))

    for person in people:
        person_obj = [p for p in people_instance_list
                      if p.name == person.get("name")]
        if person.get("wife", None) is not None:
            wife_obj = [p for p in people_instance_list
                        if p.name == person.get("wife")]
            person_obj[0].wife = wife_obj[0]
        elif person.get("husband", None) is not None:
            husband_obj = [p for p in people_instance_list
                           if p.name == person.get("husband")]
            person_obj[0].husband = husband_obj[0]

        Person.people[person_obj[0].name] = person_obj[0]
    return people_instance_list


people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]
