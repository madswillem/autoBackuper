import subprocess
from datetime import date

def startbackup():
    today = date.today()
    ctoday = str(today).replace("-", "")
    subprocess.Popen('tar -czf /run/media/mads/Backup/backup' + ctoday + '.tar.gz $HOME/Documents  $HOME/StudioProjects', shell=True)


def main():
    c = input(">>")
    if c == "start":
        startbackup()

main()