
from gamelib import *

game = Game(800,600, " Unlock! ",40)
bk = Image("Wallpaper.jpg",game)
bk.resizeTo(game.width,game.height)
bk.draw()
game.drawText("Unlock!",game.width/2 ,game.height/2,Font(black,120,yellow))
game.drawText("Press [SPACE] to play",320,400)
game.update()
game.wait(K_SPACE)
game.setBackground(bk)
#game.displayTime("Time: " + str(game.score),450,500,Font(black,120,yellow)
villan = Animation("villan.png",48
                   ,game,400/6,727/8)

ali = []
for times in range(5):
    ali.append(Image("alligator1.jpg",game))
   
villan.moveTo(125,480)
while not game.over:
    game.processInput()
    bk.draw()
    villan.draw()
    villan.resizeTo(45,45)
    for a in ali:
        a.resizeTo(40,40)
        ang = randint(45,135)
        a.setSpeed(1,ang)
        x = randint(50,750)
        y = randint(50,550)
        a.moveTo(x,y)
        a.draw()


   
    
 #if keys.pressed(K_SPACE):

    if keys.Pressed[K_RIGHT]:
        villan.moveX(8)
    if keys.Pressed[K_UP]:
        villan.moveY(-8)
    if keys.Pressed[K_LEFT]:
        villan.moveX(-8)
    if keys.Pressed[K_DOWN]:
        villan.moveY(8)
    for a in ali:
        


    

     game.update(13)



game.quit() 




           




























