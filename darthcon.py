from mcrcon import MCRcon
codes = ['§1','§2','§3','§4','§5','§6','§7','§8','§9','§c','§a','§f','§r']
fc = 0
ip = input('Server IP: ')
pas = input('Password: ')
mcr = MCRcon(ip, pas)
mcr.connect()
connected = True
print('Logged in')
while connected:
    comm = input('> ')
    if comm != 'rconlog':
        resp = mcr.command(comm)
        while fc != 13:
            resp = resp.replace(codes[fc], '')
            fc = fc + 1
        print(resp)
        fc = 0
    else:
        mcr.disconnect()
        connected = False