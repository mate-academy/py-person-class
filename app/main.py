class Person:
    people = {}

    def __init__(
        self,
        name: str,
        age: int,
    ) -> None:
        self.name = name
        self.age = age
        new_instance = {name: self}
        self.people.update(new_instance)


def create_person_list(people: list) -> list:
    new_objects = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        for key, value in person.items():
            if key == "wife" and value is not None:
                setattr(new_person, key, value)
            elif key == "husband" and value is not None:
                setattr(new_person, key, value)
        new_objects.append(new_person)

    for obj_i in range(len(new_objects)):
        person_dict = new_objects[obj_i].__dict__
        for obj_j in range(len(new_objects)):
            if "wife" in person_dict:
                if new_objects[obj_i].wife == new_objects[obj_j].name:
                    new_objects[obj_i].wife = new_objects[obj_j]
            if "husband" in person_dict:
                if new_objects[obj_i].husband == new_objects[obj_j].name:
                    new_objects[obj_i].husband = new_objects[obj_j]

    return new_objects
