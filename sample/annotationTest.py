from functools import wraps
import inspect;

class ControllerMeta(type):
    def __new__(meta, classname, supers, classdict):
        #print("META_NEW")
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print("META_INIT")
        #print ("Supers" + str(supers))
        #print(classdict)

def get(f):
    foo = "test"
    bar = 2
    nano = [1, 2, 3, 4]

    foo = foo.upper();
    print(inspect.stack()[1]);



class ActionDescriptor(object):
    def __call__(self, *args, **kwargs):
        method  = args[1].lower()
        context = args[0]
        return getattr(self, method)(context)


class ActionHandler(object):
    def __init__(self):
        #print("ActionHandler")
        self._descriptors = {}

    def get(self, f):
        #print(inspect.stack())
        descriptor = None

        if f.__name__ not in self._descriptors:
            descriptor = ActionDescriptor()
            setattr(descriptor, "method", f.__name__)
            self._descriptors[f.__name__] = descriptor
        else:
            descriptor = self._descriptors[f.__name__]

        setattr(descriptor, "get" , f)
        return descriptor

    def post(self, f):
        descriptor = None
        if f.__name__ not in self._descriptors:
            descriptor = ActionDescriptor()
            setattr(descriptor, "method", f.__name__)
            self._descriptors[f.__name__] = descriptor
        else:
            descriptor = self._descriptors[f.__name__]

        setattr(descriptor, "post" , f)
        return descriptor

    def register(self, method):
        method = method.lower()

        def wrapper(f):
            descriptor = None
            if f.__name__ not in self._descriptors:
                descriptor = ActionDescriptor()
                setattr(descriptor, "method", f.__name__)
                self._descriptors[f.__name__] = descriptor
            else:
                descriptor = self._descriptors[f.__name__]

            setattr(descriptor, method , f)

            return descriptor

        return wrapper


class Controller(object):
    __metaclass__ = ControllerMeta
    action        = ActionHandler()


class AboutController(Controller):
    action = ActionHandler()

    #@get
    def index(self):
        print(self)
        print("GET - ABOUT")
#
#class HomeController(Controller):
#    action = ActionHandler()
#
#    @action.get
#    def index(self):
#        print(self)
#        print("GET - HOME")



if __name__ == "__main__":
    a = AboutController()
    print a.index
    #h = HomeController()
    #a.index(a, "get")
    #h.index(h, "get")
    #print(c.index(c, "DELETE"))
    #c.index()
