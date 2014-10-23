#!/usr/bin/env python

# Here's a very rough start to the atom class.

class atom(object):
    
    def __init__(self,atom_type,num_id,position,first_nn,second_nn):
        self.atom_type = atom_type      # Fe or Ti
        self.num_id = num_id            # Number ID (1-128)
        self.position = position        # Atom's position
        self.first_nn = first_nn        # 1st nearest neighbors
        self.second_nn = second_nn      # 2nd nearest neighbors
        
        if self.atom_type == "Fe":
            self.mass = 55.845 # In amu
        elif self.atom_type == "Ti":
            self.mass = 47.867 # In amu
        
    def update_position(self):  
