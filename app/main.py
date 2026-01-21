class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    persons_instances = [
        Person(person["name"],
               person["age"])
        for person in people
    ]

    for person in people:
        instances_cache = Person.people
        person_instance = instances_cache[person["name"]]
        get_wife = person.get("wife")
        get_husband = person.get("husband")
        if get_wife:
            person_instance.wife = instances_cache[get_wife]
        elif get_husband:
            person_instance.husband = instances_cache[get_husband]

    return persons_instances
