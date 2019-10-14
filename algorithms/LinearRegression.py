import numpy as np

class RegressionAlg():

    def __init__(self):
        #Starting with a basic sin function
        self.step = 0.001

        self.a = 1
        self.b = np.pi/2
        self.c = 0
        self.d = 0
        
    def valFunc(self, x):
        return(self.a*np.sin(self.b*x-self.c)+self.d)

    def valFuncDerivative(self, x):
        return(self.a*self.b*np.cos(self.b*x-self.c))

    def train(self, training_set):
        #training_set is a list of lists with two values
        #   for each item in the list:
        #       i[0] float day of year with hours as decimal
        #       i[1] float amount of rainfall

        
        for i in training_set:
            guess = self.valFunc(i[0])
            ans = i[1]
            if ans > guess:
                self.d+=self.step
                diff = abs(ans - guess)
                self.a = self.a - (((diff/2)/self.a)*self.step)
            elif ans < guess:
                self.d-=self.step
                diff = abs(guess - ans)
                self.a = self.a + (((diff/2)/self.a)*self.step)
            else:
                continue

            dguess = self.valFuncDerivative(i[0])
            dans = self.valFuncDerivative(i[1])
            if dans > 0 and dguess > 0:
                if dans > dguess:
                    self.b+=self.step
                    self.c+=self.step
                elif dans < dguess:
                    self.b+=self.step
                    self.c-=self.step
                else:
                    continue
            elif dans < 0 and dguess < 0:
                if dans > dguess:
                    self.c+=self.step
                elif dans < dguess:
                    self.c-=self.step
                else:
                    continue
            elif dans > 0 and dguess < 0:
                self.b+=self.step
                self.c+=self.step
            elif dans < 0 and dguess > 0:
                self.b-=self.step
                self.c-=self.step
            else:
                continue
            ##print('Guessed value: {} Real Value: {}'.format(guess, ans))
            ##print('Guessed dval: {} Real dval: {}'.format(dguess, dans))

