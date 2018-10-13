import numpy as np
from percept import Percept
np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)

class MDP:
    def __init__(self):
        #Dim 1 -> Actie
        #Dim 2 -> Current State
        #Dim 3 -> Next State
        #Dim 4 -> Waardes
        self._tables = np.zeros((16, 4, 16, 4))

    @property
    def matrix(self):
        return self._tables

    def update(self, percept : Percept):
        #Update R(reward), zit in percept, element 0
        #Update Nsa(state actie frequentie), hoe vaak hebben we op deze staat deze actie uitgevoert
        #Update Ntsa(state s-actie-state s' frequencties
        #Update Ptsa (update transitiemodel, maw wat is da kans dat ik hier uitglij?)
        #self.matrix[percept.current_state,percept.action,percept.next_state]
        self.matrix[percept.current_state, percept.action, percept.next_state, 0] = percept.reward
        self.matrix[percept.current_state,percept.action, ::, 1:2] =  self.matrix[percept.current_state,percept.action, ::, 1:2] + 1
        self.matrix[percept.current_state, percept.action, percept.next_state, 2] = self.matrix[percept.current_state, percept.action, percept.next_state, 2] + 1
        self.matrix[percept.current_state, percept.action, percept.next_state, 3] = 0

        Nsa = self.matrix[percept.current_state, percept.action, percept.next_state, 1]
        Ntsa = self.matrix[percept.current_state, percept.action, percept.next_state, 2]
        self.matrix[percept.current_state, percept.action, percept.next_state, 3] = Ntsa / Nsa

