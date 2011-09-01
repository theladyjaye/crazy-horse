from crazyhorse.features.requests.form_parser import FormParser
from crazyhorse.features.params import ParamCollection

def feature_forms(context):
    content_length = -1

    try:
        content_length = int(context.environ.get("CONTENT_LENGTH", "0"))
    except ValueError:
        pass

    if content_length > 0:
            parser = FormParser()
            values = {"content_type":context.environ.get("CONTENT_TYPE", "application/unknown"),
                      "length": content_length,
                      "data":context.environ["wsgi.input"]}

            # merge a dictionary:
            # http://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-as-a-single-expression

            data = ParamCollection(parser.parse_body(**values))
            context.request.data = data
            print("----------------{0}-------------".format(content_length))
            for x in data:
                print("{0}: {1}".format(x, data[x]))
            # TODO handle files
            #if len(parser.files) > 0:
            #    self.files.update(parser.files)