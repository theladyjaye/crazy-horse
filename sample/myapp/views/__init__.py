from jinja2 import Environment, PackageLoader
jinja2 = Environment(loader=PackageLoader('myapp', 'views'))


class Jinja2View(object):

    def __init__(self, name, model):
        self.view_name = name
        self.model     = model;

    def __call__(self):
        # can apply caching logic here if needed
        #response = self.context.response
        template = jinja2.get_template(self.view_name)

        # View Results should be responsible for setting the content type, not the controllers

        response.headers.add("content-type", "text/html", charset="utf-8")
        return template.render(self.model)#+ "<pre>{0}</pre>".format(str(self.context.environ))
