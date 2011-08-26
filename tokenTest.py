import time
import re
def action1():
    print("action1")


def action2():
    print("action2")


def action3():
    print("action3")


def action4():
    print("action4")


def action5():
    print("action5")


def action6():
    print("action6")


class RouteTree(object):

    def __init__(self):
        self.tree = {}

    def add_route(self, route):
        leaf = self.process_route_token(route.token)
        leaf["route"] = route

    def process_route_token(self, token, location=None):

        if location is None:
            location = self.tree

        if token.value in location:
            location = location[token.value]
        else:
            location[token.value] = {}
            location = location[token.value]

        if token.next is not None:
            location = self.process_route_token(token.next, location)

        return location


    def route_with_path(self, path):

        parts  = path.split("/")
        token  = RouteToken(parts[0])

        [token.append_segment(segment) for segment in parts[1:]]
        node    = self.tree
        current = token
        route   = None

        while True:
            if current.value in node:
                node    = node[current.value]
                if current.next is not None:
                    current = current.next
                    continue
                else:
                    route =  node["route"]
                    return route
            else:
                return route




class Route(object):

    def __init__(self, url, action):
        self.url    = url
        self.action = action
        self.token  = None
        self.process_url()

    def process_url(self):
        parts      = self.url.split("/")
        self.token = RouteToken(parts[0])

        for segment in parts[1:]:
            self.token.append_segment(segment)



class RouteToken(object):

    def __init__(self, segment):
        self._value       = segment
        self.next         = None
        self.current_leaf = None

    @property
    def value(self):
        return self._value

    def append_segment(self, segment):
        token = RouteToken(segment)

        if self.next is None:
            self.current_leaf = token
            self.next         = self.current_leaf
        else:
            self.current_leaf.next = token
            self.current_leaf      = token


route_tree = RouteTree()
routes = [{"url":"our-products", "action":action1},
          {"url":"our-products/juice", "action":action2},
          {"url":"our-products/juice/green-machine", "action":action3},
          {"url":"our-products/water/coconut-water", "action":action4},
          {"url":"our-products/soup/very-veggie", "action":action5},
          {"url":"our-products/juice/blue-machine", "action":action5},
          {"url":"our-products/juice/red-machine", "action":action5},
          {"url":"our-products/juice/purple-machine", "action":action5},
          {"url":"our-products/juice/oj", "action":action5},
          {"url":"our-products/juice/peach-mangosteen", "action":action5},
          {"url":"fresh-news", "action":action6}]

# lex up the urls
for r in routes:
    route = Route(**r)
    route_tree.add_route(route)


routes.append({"url":"our-products/foo/bar/baz"})

print("tree search:")
t0 = time.clock()
for i in range(1000):
    for r in routes:
        route = route_tree.route_with_path(r["url"])
        #if route == None:
        #    print(404)
        #else:
        #    route.action()
print("execution time: " + str(time.clock() - t0) + " seconds\n")

re_tree = [
           {"pattern":re.compile(r"^our-products/[a-zA-Z-]+/[a-zA-Z-]+$"), "action":action3},
           #{"pattern":re.compile(r"^our-products/juice/blue-machine$"), "action":action3},
           #{"pattern":re.compile(r"^our-products/juice/red-machine$"), "action":action3},
           #{"pattern":re.compile(r"^our-products/juice/purple-machine$"), "action":action3},
           #{"pattern":re.compile(r"^our-products/juice/oj-machine$"), "action":action3},
           #{"pattern":re.compile(r"^our-products/juice/peach-mangosteen$"), "action":action3},
           #{"pattern":re.compile(r"^our-products/water/coconut-water$"), "action":action4},
           #{"pattern":re.compile(r"^our-products/soup/very-veggie$"), "action":action5},
           {"pattern":re.compile(r"^our-products/[a-zA-Z-]+$"), "action":action2},
           {"pattern":re.compile(r"^our-products$"), "action":action1},
           {"pattern":re.compile(r"^fresh-news$"), "action":action6}
           ]

print("regular expression search:")
t0 = time.clock()
for i in range(1000):
    for r in routes:
        action = None

        for obj in re_tree:
            pattern = obj["pattern"]
            if pattern.match(r["url"]):
                action = obj["action"]
                break

        #if action == None:
        #    print(404)
        #else:
        #    action()

print("execution time: " + str(time.clock() - t0) + " seconds\n")



