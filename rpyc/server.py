import rpyc
port = 18861

class MyService(rpyc.Service):
    def on_connect(self, conn):
        print ( 'connected on port', port)

    def on_disconnect(self, conn):
        pass

    # operação sem argumentos e sem valor de retorno
    def exposed_method1(self): 
        pass

    # operação com um argumento long e valor de retorno long 
    def exposed_method2(self, number): 
        return number*number

    # operação com oito argumentos long e valor de retorno long 
    def exposed_method3(self, n1, n2, n3, n4, n5, n6, n7, n8): 
        return int((n1+n2+n3+n4+n5+n6+n7+n8)/8 )
    
    # operação com oito argumentos long e valor de retorno long 
    def exposed_method4(self, s1, s2, s3, s4):
        return s1+s2+s3+s4


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=port)
    t.start()