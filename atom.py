#!/usr/bin/env python

# Here's a very rough start to the atom class. Haven't dealt with nearest neighbors yet.

class atom(object):
    
    def __init__(self,atom_type,num_id,position):
        self.atom_type = atom_type
        self.num_id = num_id
        self.position = position
        
        if self.atom_type == "Fe":
            self.mass = 55.845 # In amu
        elif self.atom_type == "Ti":
            self.mass = 47.867 # In amu
        
    def update_position(self):  
