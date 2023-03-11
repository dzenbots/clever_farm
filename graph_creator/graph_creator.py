from matplotlib import pyplot


class GraphCreator:
    def __init__(self):
        self.creator = pyplot

    def create_graph(self, data: list, output_filename: str):
        self.creator.figure(figsize=(20, 4 * len(data)))
        for i in range(0, len(data)):
            self.creator.subplot(len(data), 1, i + 1)
            self.creator.plot(data[i].get('data_x'), data[i].get('data_y'))
            self.creator.title(data[i].get('label'))
        self.creator.savefig(output_filename)
