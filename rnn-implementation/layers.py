from activation import Tanh
from gate import AddGate, MultiplyGate

mulgate = MultiplyGate()
addgate = AddGate()
tanh = Tanh()

class RNNLayer:
    def foward(self, x, prev_a, waa, wax, wya):
        self.mulax = mulgate.forward(wax, x)
        self.mulaa = mulgate.forward(waa, prev_a)
        self.add = addgate.forward(self.mulax, self.mulaa)
        self.a = tanh.forward(self.add)
        self.mulya = mulgate.forward(wya, a)

## dmulya = y^t - yt
    def backward(self, x, prev_a, waa, wax, wya, diff_a, dmulya):
        self.forward(x, prev_a, waa, wax, wya)
        dV, ds = mulgate.backward(wya, self.a, dmulya)
        

        
        