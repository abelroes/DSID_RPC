import rpyc

c = rpyc.connect("localhost", 18861)

print( c.root.method1() )
print( c.root.method2(25) )
print( c.root.method3(5,5,5,10,25,5,5,5) )
print( c.root.method4("a", "b", "c", "d") )