import os

class Ping:
    def execute(self, ip):
        if ip.startswith('192.'):
            for i in range(10):
                response = os.system("ping -n 2 " + ip)
                if response == 0:
                    print(ip, 'es accesible')
                else:
                    print(ip, 'no es accesible')
        else:
            print('Error: la direccion IP no comienza con 192.')
    
    def executefree(self, ip):
        for i in range(10):
            response = os.system("ping -n 2 " + ip)
            if response == 0:
                print(ip,'es accesible')
            else:
                print(ip,'no es accesible')

class PingProxy:
    def __init__(self):
        self.ping = Ping()
        
    def execute(self, ip):
        if ip == '192.168.0.254':
            self.ping.executefree('www.google.com')
        else:
            self.ping.execute(ip)

p = PingProxy()

p.execute('192.168.0.254')