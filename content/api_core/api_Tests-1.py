from discretize import tests, utils
import numpy as np

def simplePass(x):
    return np.sin(x), utils.sdiag(np.cos(x))
tests.checkDerivative(simplePass, np.random.randn(5))