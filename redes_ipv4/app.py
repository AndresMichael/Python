from calc_ipv4 import CalcIPV4
# tem que retornar rede, broadcast, prefixo e n° de ips válidos

rede1 = CalcIPV4('192.168.0.25', cidr=26)
print(rede1.ip)
print(rede1.mask)
print(rede1.cidr)
print(rede1.ips_validos)
print(rede1._set_broadcast())
print(rede1.rede)
