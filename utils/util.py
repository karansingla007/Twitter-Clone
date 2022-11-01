import uuid


def getTweetId():
    randomId = uuid.uuid4().hex[:8]
    return randomId

