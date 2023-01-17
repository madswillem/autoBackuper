import subprocess
import shlex

def startbackup(language):
    subprocess.call(shlex.split('./backup.sh '+language))


def main():
    print('Commands:                                    ')
    print('                                             ')
    print('exit|quit|q|stop         To Exit the Backuper')
    print('start [Systemlanguage]   Start the Backup    ')
    print('                                             ')
    c = input(">>")

    x = c.split(" ")

    if x[0] == "start":
        print(x[1])
        startbackup(x[1])
    if x[0] == "exit" or "quit" or "q" or "stop":
        exit()

main()