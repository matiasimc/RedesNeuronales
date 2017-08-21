class Network:
    def __init__(self):
        self.layers = []

    def addLayer(self,layer):
        self.layers.append(layer)

    def update(self, inputs):
        for l in self.layers:
            l.update(inputs)
