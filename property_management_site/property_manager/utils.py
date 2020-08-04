import uuid

default_salt = 'some-salt'

def create_new_id():
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, default_salt))
