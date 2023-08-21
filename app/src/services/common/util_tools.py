from threading import RLock

single_lock = RLock()


# Used to create single class object
def singletonType(cls):
    instance = {}

    def _singleton_wrapper(*args, **kwargs):
        with single_lock:
            if cls not in instance:
                instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return _singleton_wrapper
