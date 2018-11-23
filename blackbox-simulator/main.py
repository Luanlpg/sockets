import socket
import time
import sys

class MySocketBlackBox:
    """
    Classe que simula comportamento da blackbox, enviando msg via socket
    ex: SSSSSSSSSSSSSSSS E R R R R DDDD-DD-DD TT:TT:TT.TTT
    S = Serial
    E = Energized
    R = Relay
    D = Date
    T = Time
    """

    def __init__(self, h, p):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dest = (h, p)
        # tenta conecção
        try:
            self.udp.connect(self.dest)
        # caso não consiga, printa "ERRO DE CONECÇÃO!"
        except Exception as e:
            print('-----------ERRO DE CONECÇÃO!------------')


    def send_payload_fake(self, msg):
        """Envia payload falso via socket"""
        return self.udp.send(msg)


    def exec(self):
        """
        Cria lista com msgs a serem enviadas e para cada uma delas chama o
        método send_payload_fake para envia-la.
        """

        lista = [
            b'00000000c3cc00bb 0 1 1 0 0 2018-11-22 14:47:58.000',
            b'0000000005bf040f 1 0 1 0 0 2018-11-22 14:47:58.000',
            b'00000000aa630cd9 1 0 0 0 0 2018-11-22 14:47:59.000',
            b'000000001b818125 0 0 0 1 0 2018-11-22 14:47:59.000',
            b'000000009853c23a 1 1 1 0 0 2018-11-22 14:47:59.000',
            b'00000000c1c9f712 1 0 0 1 0 2018-11-22 14:48:00.000',
            b'00000000f30dbc34 1 1 0 0 0 2018-11-22 14:48:00.000',
            b'00000000c7dbc85a 1 1 1 0 0 2018-11-22 15:00:08.000'
            ]
        try:
            # para cada msg na lista de msgs uma msg é enviada
            for msg in lista:
                self.send_payload_fake(msg)
                # pausa o laço de 3 em 3 seg.
                time.sleep(3)
        # caso Ctrl+C seja pressionado o programa para.
        except KeyboardInterrupt:
            x = False
            self.udp.close()
            print("Ctrl+C pressionado, encerrando aplicação e saindo...")
            sys.exit(0)

x = True
if __name__ == '__main__':
    print('--SIMULADOR SMARTBOX--')
    host = str(input('host: '))
    port = int(input('port: '))
    print('Enviando payloads, pressione Ctrl+C para cancelar...')
    black_box = MySocketBlackBox(host, port)
    # laço infinito, a não ser que KeyboardInterrupt seja acionada
    while x:
        black_box.exec()
