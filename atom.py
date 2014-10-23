#!/usr/bin/env python

# Here's a very rough start to the atom class.

from numpy import *

class atom(object):
    
    def __init__(self, num_id, xdatcar):
        self.num_id = num_id            # Number ID (1-128)
        
        self.xdatcar = xdatcar          # This is the string with the name of the XDATCAR file
        self.f = open(self.xdatcar,"r")
        
        for i in range(7+self.num_id):
            self.f.readline()           # Skip to line with num_id's position
        
        line = self.f.readline()        # The line with num_id's position in XDATCAR
        
        self.position = array((float(line[3:13]),float(line[15:25]),float(line[27:37])))
                
        if self.num_id <= 64:           # Fe: #1-64
            self.mass = 55.845 # In amu
        else:                           # Ti: #65-128
            self.mass = 47.867 # In amu
        
        # The next variables will be lists containing the num_ids of the nearest neighbors
        self.first_nn = []
        self.second_nn = []        
        
    def get_neighbors(self):
        
        # Getting the num_ids of the first neighbors.        
        for i in range(1,129):
            diff = abs(atom(i,self.xdatcar).position - self.position)            
                
            if (diff == array((.125,.125,.125))).all() or (diff == array((.875,.125,.125))).all() or \
            (diff == array((.125,.875,.125))).all() or (diff == array((.125,.125,.875))).all() or \
            (diff == array((.875,.875,.125))).all() or (diff == array((.875,.125,.875))).all() or \
            (diff == array((.125,.875,.875))).all() or (diff == array((.875,.875,.875))).all():
                self.first_nn.append(i)                  
        
    def update_position(self):        
        pass
    
    self.f.close() # Close xdatcar file
