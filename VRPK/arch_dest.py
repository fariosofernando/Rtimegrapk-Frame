import shutil
import time

path_init = '/home/root3/Área de Trabalho/projeto meu beat/code/kivy_file.kv'
path_nitial = 'parte_grafica/File.kv'


while True:
    time.sleep(2)
    shutil.copy('parte_grafica/File.kv', path_init)
    print('destribuidor está a funcionar')

    # with open (path_init, 'r') as read:
    #     READ = read.read()

    # with open (path_nitial,'r') as read_:
    #     READ_ = read_.read()


    # if READ != READ_:
    #     print('destribuidor parou, Esperando retoma da ligacao')
    #     shutil.copy(path_init, path_nitial)
    #     print('Ligacao retomada, relaxe...')
  
    # elif READ == READ_:
    #     shutil.copy('parte_grafica/File.kv', path_init)
    #     print('destribuidor está a funcionar')