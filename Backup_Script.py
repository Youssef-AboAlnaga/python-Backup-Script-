from netmiko import ConnectHandler
from os import path
from sys import argv



#Print banner---------------------------------------------------------------------------
print ("""
****************************************************************
                        Company Banner
****************************************************************
                                                               Powered By: Youssef Ahmed
""")

#Get info.txt file Path to read data ----------------------------------------
info = open(path.dirname(path.abspath(argv[0]))+"{}".format("\info.txt"), "r")

#convert data of file to dictionary to can split it------------------------------------
dic_content = eval(info.read())

#store data from file to variables to call him function------------------------------
DestinationDirectory = "{}".format(dic_content['directory'])
Username = "{}".format(dic_content['username'])
Password = "{}".format(dic_content['password'])
EnablePassword = "{}".format(dic_content['secret'])
DeviceList = eval("{}".format(dic_content['devices']))


#select individual ips and open it by SSH to get running config to restore it---------
for ip in DeviceList:

  #function that establish connection using ip and restore running config--------------
  def GetBackup(ip):

      #we use TRY and EXCEPT to reduce the errors-------------------------------------
      try:

          #start SSH connection using ip that get it from function---------------------
          connection = ConnectHandler(ip="{}".format(ip), device_type="cisco_ios", username="{}".format(Username), password="{}".format(Password), secret="{}".format(EnablePassword))
          connection.enable()
          show_runn = connection.send_command(" sh run ")


          #get hostname of devices to write it in filename---------------------------
          output = connection.send_command('sh run | i host')
          output = output.split()


          #open txt file and name it by ip & name and write show running in it---------
          opentxt = open(DestinationDirectory+"{0} ( {1} ).txt".format(ip,output[1]), 'a')
          opentxt.write(show_runn)
          opentxt.close()
          #close the file--------------------------------------------------------------

          connection.disconnect()
          #close connection------------------------------------------------------------

          print(" The backup has been successfully taken from ( {0} ) device called {1}                        ( Done )".format(ip, output[1]))

      except:

          print(" There is an error in the script in extracting the device's backup ( {0} )                    ( Failed )".format(ip))

  #call Function----------------------------------------------------------------------
  GetBackup(ip)




print("""
****************************************************************************************
**                                     End Script                                     **
****************************************************************************************
""")

