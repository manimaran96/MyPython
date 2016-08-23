"""Sub and Super Class"""
#Parent class
class pclass:
    var1="i love all"
    var2="i hate love"

#child class of pclass
class cclass(pclass):
    pass

pobj=pclass()
cobj=cclass()

print "Parent class called"
print pobj.var1
print pobj.var2

print "Child class called"
print cobj.var1
print cobj.var2
