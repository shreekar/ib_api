class AnyWrapper(object):
    @staticmethod
    def error(msg):
        return msg

    @staticmethod
    def build_error(error_id, error_code, error_msg):
        return "%d | %d | %s" % (error_id, error_code, error_msg)

    @staticmethod
    def connection_closed():
        return 'Connection Closed'
