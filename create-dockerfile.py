users = []
try:
    from users import users
except ModuleNotFoundError:
    print('No module \'users\' found.')
    if 'y' == input('Would you like to enter users manually (y/n)? '):
        user = input('User (ENTER to quit): ')
        while user != '':
            users.append(user)
            user = input('User (ENTER to quit): ')
    else:
        print('No Dockerfile written.')
        exit(1)

from sys import argv
import os

if __name__ == '__main__':
    if '--help' in argv:
        print(f'{os.path.basename(__file__)} [optional password]')
        print('  If no password is given, the default password for each user')
        print('  will be their username.')
        exit(0)

    default_password = ''
    if len(argv) == 2:
        default_password = argv[1]
    
    with open('Dockerfile', 'w') as f:
    
        f.write('FROM ubuntu:latest\n')
        f.write('RUN apt update && apt install openssh-server sudo -y\n')
        f.write('RUN apt install vim -y\n')
    
        uid = 1000
        for u in users:
            f.write(f'RUN useradd -rm -d /home/{u} -s /bin/bash ' +
                    f'-g root -G sudo -u {uid} {u}\n') 
            uid += 1
            password = default_password if default_password else u
            f.write(f'RUN  echo \'{u}:{password}\' | chpasswd\n')
    
    
        f.write('RUN service ssh start\n')
    
        f.write('EXPOSE 22\n')
    
        f.write('CMD ["/usr/sbin/sshd","-D"]\n')

    print('Output written to Dockerfile')


