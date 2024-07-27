class Injective(dict):
    def __init__(self, *args, **kwargs) -> None:
        super(Injective, self).__init__(*args, **kwargs)

    def inverse(self):
        """
        Returns the inverse dict
        :return: inverse: dict
        """

        used_keys: set = set()
        def ensure_unique(key):
            if key in used_keys:
                raise KeyError(f'Dictionary is not one-to-one')
            used_keys.add(key)
            return key

        return Injective({ensure_unique(v): k for k, v in super(Injective, self).items()})
