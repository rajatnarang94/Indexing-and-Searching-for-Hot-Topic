#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:43:11 2019

@author: smore
"""

import hashlib

class MinCount:
    
    def __init__(self, d, w):
        self.d = 2000
        self.w = 7
        self.cms = [[0 for _ in range(self.w)] for _ in range(self.d)]
        
    def insertCMS(self, word):
        hash1 = int(int(hashlib.sha1(word.encode('utf-8')).hexdigest(),16) % self.d)
        hash2 = int(int(hashlib.sha224(word.encode('utf-8')).hexdigest(),16) % self.d)
        for i in range(self.w):
            hash_val = (hash1 + (i*hash2)) % self.d
            self.cms[hash_val][i] += 1
            
    def count(self, word):
        hash1 = int(int(hashlib.sha1(word.encode('utf-8')).hexdigest(),16) % self.d)
        hash2 = int(int(hashlib.sha224(word.encode('utf-8')).hexdigest(),16) % self.d)
        store = []
        for i in range(self.w):
            hash_val = (hash1 + (i*hash2)) % self.d
            store.append(self.cms[hash_val][i])
        return min(store)
