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

