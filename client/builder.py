class Builder(object):
    """
        This class is used to build messages so the entire message
    can be sent to the socket in a single write.
    """
    SEP = 0