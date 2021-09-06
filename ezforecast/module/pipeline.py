import os
import logging


class Pipeline(object):
    """
        Pipeline instance
    """
    def __init__(self, *args, **kwargs):
        super(Pipeline, self).__init__()
        self.layers = list()
        
        for layer in args:
            self.layers.append(layer)

    def append(self, layer):
        """
        Append a layer to pipeline
        
        :param layer: Must be a callable layer
        :return: None
        """
        
        self.layers.append(layer)

    def keyword_arguments(self):
        """
        Return pipeline's protected attribute and its value in form of dictionary

        :return: key-value of protected attribute
        :rtype: Dict
        """

        return {attr[11:]: getattr(self, attr) for attr in dir(self) if attr[:10] == '__Pipeline__' and getattr(self, attr) is not None}

    def forward(self, *args, **kwargs):
        """
        Execute all callable layer in self.layers

        :param args:
        :param kwargs:
        :return:
        """
        
        x = None
        for layer in self.layers:
            x = layer(x, *args, **kwargs, **self.keyword_arguments())

        return x

    def save(self, save_path: str):
        """
        Save pipeline to disk

        :param save_path: path to save model
        :return: None
        """

        import dill
        with open(save_path, "wb") as stream:
            dill.dump(self, stream)
            print(f"Save model to {save_path}")

    @staticmethod
    def load(save_path: str):
        """
        Load model from disk

        :param save_path: path to saved pipeline
        :return:
        """

        import dill
        assert os.path.exists(model_path), FileNotFoundError(f"Could not found {save_path}")

        with open(save_path, "rb") as stream:
            print(f"Loaded pipeline from {save_path}")
            return dill.load(stream)

