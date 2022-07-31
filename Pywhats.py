import pywhatkit as kt
import getpass as gp


#kit.playonyt('Jhon Lennon')

"""print("let's automate with python")

p_num = gp.getpass(prompt='phone number: ',stream=None )

msg = "I love you"

kt.sendwhatmsg(p_num, msg, 5, 30)"""

try:
   
  # sending message to receiver
  # using pywhatkit
  kt.sendwhatmsg("+919535202224", "Hello from GeeksforGeeks", 3, 28)
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")