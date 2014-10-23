#!/usr/bin/env python

# Here's a very rough start to the atom class.

from numpy import *

class atom(object):
    
    def __init__(self, atom_type, num_id, xdatcar):
        self.atom_type = atom_type      # Fe or Ti
        self.num_id = num_id            # Number ID (1-128)
        
        self.xdatcar = xdatcar          # This is the string with the name of the XDATCAR file
        self.f = open(self.xdatcar,"r")
        
        for i in range(7+self.num_id):
            self.f.readline()           # Skip to line with num_id's position
        
        line = self.f.readline()        # The line with num_id's position in XDATCAR
        
        self.position = array((float(line[3:13]),float(line[15:25]),float(line[27:37])))
        
        
        if self.atom_type == "Fe":
            self.mass = 55.845 # In amu
        elif self.atom_type == "Ti":
            self.mass = 47.867 # In amu
        
    def update_position(self):  
