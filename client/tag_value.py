class TagValue(object):
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value
