class Injective(dict):
    def __init__(self, *args, **kwargs) -> None:
        super(self.__class__).__init__(*args, **kwargs)

    def inverse(self) -> dict:
        """
        Returns the inverse dict
        :return: inverse: dict
        """

        return dict([(v, k) for k, v in super(Injective, self).items()])
