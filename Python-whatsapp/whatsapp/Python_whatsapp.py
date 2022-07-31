from distutils.command.check import check
import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)
position1 = pt.locateOnScreen(r"C:\Users\503266786\Documents\Python-AI\Python-whatsapp\whatsapp\Capture_payperclip.png", confidence=.6)

x = position1[0]
y = position1[1]

print(x,y)


#gets message

def get_message():
    global x, y

    position = pt.locateOnScreen(r"C:\Users\503266786\Documents\Python-AI\Python-whatsapp\whatsapp\Capture_payperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x + 70, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()

    whatsapp_msg = pyperclip.paste()
    pt.click()
    print("Message received: " + whatsapp_msg)




# Posts

def post_message(message):
    global x, y

    position = pt.locateOnScreen(r"C:\Users\503266786\Documents\Python-AI\Python-whatsapp\whatsapp\Capture_payperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)
    pt.typewrite("\n", interval=.01)
    pt.click()



#process responses

def process_responses(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "don't ask me any question"
    else:
        if random_no == 0:
            return "that's cool"
        elif random_no ==2:
            retrun "what are you doing"
        else:
            return "I want something"



#check for new messages

def check_for_new_messages():
    pt.moveTo( x + 50, y - 35, duration=.5)


    while True:
        #continuously checks for team messages
        try:
            position = pt.locateOnScreen(r"C:\Users\503266786\Documents\Python-AI\Python-whatsapp\whatsapp\group.png", confidence=.9)

            if position is not None:
                pt.moveTo(position)
                pt.movRel(-100,0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("no new messages located")

        if pt.pixelMatchesColor(int(x), int(y), (255, 255, 255), tolerance=10)
            print("is white")
           

            processed_response = process_response(get_message())

            post_response(processed_response)
        else:
             print("there are no new messages")

         sleep(5)


check_for_new_messages()




 




