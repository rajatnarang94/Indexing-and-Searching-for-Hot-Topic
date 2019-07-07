#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:36:00 2019

@author: smore
"""


from nltk.corpus import stopwords 
import hashlib

class BloomFilter:
    
    def __init__(self, n, m, k):
        self.stop_words = ["ned", "eddard", "robert", "jamie", "catelyn", "cersei", "daenerys", "jorah", "viserys", "jon", "sansa", "arya", "theon", "bran", "joffrey", "tyrion", "baelish", "davos", "samwell", "stannis", "melisandre", "jeor", "bronn", "varys", "tywin", "gendry", "brienne", "ramsay", "gilly", "daario", "missandei"]
        
        self.n = n
        self.m = m
        self.k = k
        self.bloom = [False for _ in range(m)]
    
    def createBloom(self):
        for word in self.stop_words:
            hash1 = int(int(hashlib.sha1(word.encode('utf-8')).hexdigest(),16) % self.m)
            hash2 = int(int(hashlib.sha224(word.encode('utf-8')).hexdigest(),16) % self.m)
            for i in range(self.k):
                hash_val = (hash1 + (i*hash2)) % self.m
                if not self.bloom[hash_val]:
                    self.bloom[hash_val] = True
                
    def checkBloom(self, word):
        hash1 = int(int(hashlib.sha1(word.encode('utf-8')).hexdigest(),16) % self.m)
        hash2 = int(int(hashlib.sha224(word.encode('utf-8')).hexdigest(),16) % self.m)
        for i in range(self.k):
            hash_val = (hash1 + (i*hash2)) % self.m
            if not self.bloom[hash_val]:
                return False
        return True

