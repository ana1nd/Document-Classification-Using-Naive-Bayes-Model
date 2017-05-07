from __future__ import division
from math import *

def calculate(n11,n10,n01,n00):
    n1=n10+n11
    n0=n01+n00
    n=n11+n10+n01+n00
    #print n,n1,n0
    a=0
    b=0
    c=0
    d=0
    if n11!=0:
        a=(n11/n)*(log((n*n11)/(n1*n1),2))
    if n01!=0:
        b=(n01/n)*(log((n*n01)/(n0*n1),2))
    if n10!=0:
        c=(n10/n)*(log((n*n10)/(n1*n0),2))
    if n00!=0:
        d=(n00/n)*(log((n*n00)/(n0*n0),2))
    #print a,b,c,d
    ans=a+b+c+d
    return ans
