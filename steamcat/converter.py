class PriceConverter:
    regex = '[0-9]+{7}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)