
                                   *** Notes ***
                                          
This script will help us to take backups of our Cisco routers and switches, depending on 
some information that we add to it through an external file called ("info.txt") and give 
it some information such as where the backups are stored ("path"), the name and password 
of the SSH and the IPs of the devices to take backups.

1- the "info.txt" must be in the same directory beside "Backup_Script.py"
2- create user read only on AAA server with priviledge read only and make sure that it 
   can be run command " show running "
3- follow the structure of "info.txt"
     {
     "directory":"C:\\Backups\\Network\\Jun-2021\\",
     "username":"youssef",
     "password":"youssef",
     "secret":"youssef",
     "devices":["192.168.1.100", "192.168.1.20"]
     }
4- make sure that the path will be created from me manual previously.
5- when we will set directory on file, make sure that we replaced every "\" by "\\"
6- set username and password (secret=enable) that created.
7- make sure that we don't need a enable password or write it.
8- set list of devices that we need to take a backups from him like:
   ["192.168.10.253", "192.168.10.252", .....etc] 


9- to convert python script to .exe we can use:
    #enter to script path--------------------------------------------------
    cd C:\Users\Youssef Ahmed\Desktop\Backup script
    #don't forget to enter the script name---------------------------------
    pyinstaller Backup_Script.py --upx-dir=..\upx391w -y --onefile
