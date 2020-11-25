import pyautogui
from PIL import Image,ImageGrab #PIL->pillow
import time
#ImageGrab helps us to take screenshots. ImageGrab.grab()
#keyDown function is used to automate key pressing by gui.
#pyautogui.keyDown('Key') will press Key autotmatically.
def hit(key):
    pyautogui.keyDown(key)
    if key == "down":
       time.sleep(0.5)
       pyautogui.keyUp("down")
# def draw()
def isCollide(data):
      #draw the rectangle over birds.
      for i in range(200,350):
            for j in range(175,350):
                 if data[i,j] < 100:
                    hit("down")
                    return 
      #rectangel over cactus
      for i in range(200,400):
             for j in range(400,450):
                if data[i,j] < 100:
                     hit("up")
                     return
      return 

if __name__ == "__main__":
    print("T-REX Game is about to start in 3 seconds")
    time.sleep(3)
    hit('up')
    while True:
         image = ImageGrab.grab().convert('L') #taking screenshot and converting into the grayscale image.
         data = image.load()
         isCollide(data)
        #below code is just to debugging purpose
        #  if isCollide(data):
        #      hit("up")
        #draw the rectangle over cactus.
        #  for i in range(200,350):
        #      for j in range(350,450):
        #         data[i,j] = 0
        #  image.show()
        #  break

        #draw the rectangle over birds.
        #  for i in range(200,350):
        #      for j in range(200,350):
        #         data[i,j] = 191
        #  image.show()
        #  break

        

                     
    # image.show() #to display the image