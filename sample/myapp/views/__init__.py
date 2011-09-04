from jinja2 import Environment, PackageLoader, FileSystemLoader
#jinja2 = Environment(loader=PackageLoader('myapp', 'views'))
jinja2 = Environment(loader=FileSystemLoader(['/Users/dev/Projects/APP_CrazyHorse/sample/myapp/views']))


class Jinja2View(object):

    def __init__(self, name, model):
        self.content_type = "text/html; charset=utf-8"
        self.model        = model;
        self.view_name    = name

    def __call__(self):
        # can apply caching logic here if needed
        #response = self.context.response
        template = jinja2.get_template(self.view_name + ".html")

        # View Results should be responsible for setting the content type, not the controllers

        #response.headers.add("content-type", "text/html", charset="utf-8")
        return template.render(self.model)#+ "<pre>{0}</pre>".format(str(self.context.environ))
