
class Jinja2View(object):

    def __init__(self, context):
        self.view    = None
        self.model   = None
        self.context = context

    def __call__(self):
        # can apply caching logic here if needed
        response = self.context.response
        template = jinja2.get_template(self.view)

        response.headers.add("content-type", "text/html", charset="utf-8")
        return template.render(self.model) + "<pre>{0}</pre>".format(str(self.context.environ))


class CrazyHorseView(object):

    def __init__(self, name, model):
        self.name  = name
        self.model = model

class RedriectView(CrazyHorseView):

    def __call__(self):
        pass