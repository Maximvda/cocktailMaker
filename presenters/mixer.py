from presenters.presenter import Presenter

class Mixer(Presenter):
    def init(self):
        self._total = 0
        self.values = [0]*5
        self._myIds = {
            0: 'amaretto',
            1: 'brandy',
            2: 'rum',
            3: 'triple',
            4: 'lime'
        }
        self.ids.amaretto.name = 0
        self.ids.brandy.name = 1
        self.ids.rum.name = 2
        self.ids.triple.name = 3
        self.ids.lime.name = 4

    def update(self, value, id):
        self.values[id] = value
        # Rescale other values
        if sum(self.values) > 100:
            toReduce = sum(self.values) - 100
            self.values[id] -= toReduce
            self.ids[self._myIds[id]].value = self.values[id]
        self.total = sum(self.values)

    def create(self):
        self.app.model.makeCustom([
            int(self.ids.amaretto.value),
            int(self.ids.lime.value),
            int(self.ids.brandy.value),
            int(self.ids.rum.value),
            int(self.ids.triple.value),
        ])

    def calibrate(self):
        self.app.model.calibrate()

    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, value):
        self.ids.drinkBar.value = value
        self._total = value
