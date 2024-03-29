from connexion.apps.flask_app import FlaskJSONEncoder

from server.models.base_model_ import Model


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Model):
            dikt = {}
            for attr, _ in o.swagger_types.items():
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                if attr not in o.attribute_map:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        return FlaskJSONEncoder.default(self, o)
