#!/usr/bin/env python

# Here's a very rough start to the atom class.

from numpy import *

class atom(object):
    
    def __init__(self, num_id, xdatcar):
        self.num_id = num_id            # Number ID (1-128)
        
        self.xdatcar = xdatcar          # This is the string with the name of the XDATCAR file
        f = open(self.xdatcar,"r")
        
        for i in range(7+self.num_id):
            f.readline()           # Skip to line with num_id's position
        
        line = f.readline()        # The line with num_id's position in XDATCAR
        
        self.position = array((float(line[3:13]),float(line[15:25]),float(line[27:37])))
                
        if self.num_id <= 64:           # Fe: #1-64
            self.mass = 55.845 # In amu
        else:                           # Ti: #65-128
            self.mass = 47.867 # In amu
        
        # The next variables will be lists containing the num_ids of the nearest neighbors
        self.first_nn = []
        self.second_nn = []    
        
        f.close()
        
    def get_neighbors(self):
        
        for i in range(1,129):
            diff = abs(atom(i,self.xdatcar).position - self.position)            
            
            # Getting the num_ids of the first neighbors.        
            if (diff == array((.125,.125,.125))).all() or (diff == array((.875,.125,.125))).all() or \
            (diff == array((.125,.875,.125))).all() or (diff == array((.125,.125,.875))).all() or \
            (diff == array((.875,.875,.125))).all() or (diff == array((.875,.125,.875))).all() or \
            (diff == array((.125,.875,.875))).all() or (diff == array((.875,.875,.875))).all():
                self.first_nn.append(i)  
            
            # Getting the num_ids of the second neighbors.        
            if (diff == array((.25,0,0))).all() or (diff == array((.75,0,0))).all() or \
            (diff == array((0,.25,0))).all() or (diff == array((0,.75,0))).all() or \
            (diff == array((0,0,.25))).all() or (diff == array((0,0,.75))).all():
                self.second_nn.append(i)
            
            # Getting the num_ids of the third neighbors.        
            if (diff == array((.25,.25,0))).all() or (diff == array((.25,.75,0))).all() or \
            (diff == array((.75,.25,0))).all() or (diff == array((.75,.75,0))).all() or \
            (diff == array((.25,0,.25))).all() or (diff == array((.25,0,.75))).all() or \
            (diff == array((.75,0,.25))).all() or (diff == array((.75,0,.75))).all() or \
            (diff == array((0,.25,.25))).all() or (diff == array((0,.25,.75))).all() or \
            (diff == array((0,.75,.25))).all() or (diff == array((0,.75,.75))).all():
                self.third_nn.append(i)             
        
    def update_position(self):        
        pass
