# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 02:08:03 2021

@author: dekel
"""
import threading, queue
class ParsemathFile:
    def __init__(self) :
        self.q = queue.Queue()
     
        
    def parse(self,path):
        with open(path) as f:
            lines = f.readlines()  
            for line in lines: 
                self.q.put(line)
