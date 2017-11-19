class Activity:
    def __init__(self, name: str, utilization: float):
        self._name = name
        self._utilization = utilization

    @property
    def name(self):
        return self._name

    @property
    def utilization(self):
        return self._utilization

    class CulpritProcess:
        def __init__(self, id: int, name: str, utilization: float):
            self._id = id
            self._name = name
            self._utilization = utilization

        @property
        def id(self):
            return self._id

        @property
        def name(self):
            return self._name

        @property
        def utilization(self):
            return self._utilization

global row
global column
