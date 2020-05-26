import pygame
from atm import atm
from menu import menu
from player import Player
from button import Button
from menu import menu
from text import Text
from items import Item 
pygame.init()

shop_run = False

def draw_items(items):
    for item in items:
        item.draw()

deposit_button = Button((200, 20, 100), 125, 400, 325, 175, "Deposit", 80)
withdraw_button = Button((20, 100, 200), 450, 400, 325, 175, "Withdraw", 80)
cancel_button = Button((255, 255, 255), 845, 400, 300, 175, "Cancel", 80)



def shop_win_func():
    global shop_run
    shop_run = True
    
    shop_bkrd = True

    atm_inside = pygame.image.load(r"images\atm_inside.png")

    shop_image = pygame.image.load(r"images\shop.png")

    shop_win = pygame.display.set_mode((1280, 720))

    main_atm = atm(r"images\ATM.png", -15, 335, shop_win)

    moneyInAtm = Text(shop_win, 700, 140, main_atm.moneyInAtm,'freesansbold.ttf', 125, "$")

    man = Player(450, 650, shop_win)

    atm_open = pygame.image.load(r"images\ATM OPEN.png")

    cashbox_open = pygame.image.load(r"images\OPEN_CASHBOX.png")

    MoneyOnHand = Text(shop_win, 620, 40, man.MoneyOnHand, 'freesansbold.ttf', 50, "Money In Hand: ")
    MoneyOnHand.color = (40, 0, 240)

    lemon_6_image = pygame.image.load(r"images\6 breezers lemon.png")
    lemon_6 = Item(250, 150, lemon_6_image, 30, shop_win)

    watermalon_6_image = pygame.image.load(r"images\6 breezers watermalon.png")
    watermalon_6 = Item(600, 150, watermalon_6_image, 30, shop_win)

    lemon_1_image = pygame.image.load(r"images\breezer lemon.png")
    lemon_1 = Item(100, 150, lemon_1_image, 10, shop_win)
    
    
    watermalon_1_image = pygame.image.load(r'images\breezer watermalon.png')
    watermalon_1 = Item(450, 175, watermalon_1_image, 10, shop_win)
    
    apple_image = pygame.image.load(r"images\apple.png")
    apple = Item(820, 100, apple_image, 10, shop_win)   
 
    items = [lemon_6, watermalon_6, apple, watermalon_1, lemon_1]



    

    while shop_run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                shop_run = False

        if keys[pygame.K_LEFT] and man.x > 400:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x < 1050:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0

        

        if shop_bkrd:
            shop_win.blit(shop_image, (0,0))
            man.draw()
            shop_win.blit(main_atm.image, (main_atm.x, main_atm.y))
            if man.x in range(400, 500):
                shop_win.blit(atm_open, (300, 200))
                if keys[pygame.K_KP_ENTER]:
                    shop_bkrd = False
            elif man.x in range(900, 1100):
                shop_win.blit(cashbox_open, (300, 200))
                if keys[pygame.K_KP_ENTER]:
                    shop_bkrd = False
        elif shop_bkrd == False and man.x in range(900, 1100):
            shop_win.fill((0,0,0))
            draw_items(items)
            #* open cashbox

        elif shop_bkrd == False and man.x in range(400, 500):
            main_atm.drawATM(deposit_button, withdraw_button, cancel_button, atm_inside)
            moneyInAtm.show_text()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if deposit_button.isOver(pos):
                    main_atm.moneyInAtm += man.MoneyOnHand
                    man.MoneyOnHand = 0
                    MoneyOnHand.text = man.MoneyOnHand
                    moneyInAtm.text = main_atm.moneyInAtm
                    pygame.display.update()
                if withdraw_button.isOver(pos):
                    print("withdraw")
                if cancel_button.isOver(pos):
                    shop_bkrd = True
            if event.type == pygame.MOUSEMOTION:
                if deposit_button.isOver(pos):
                    deposit_button.color = (190, 10, 80)
                elif withdraw_button.isOver(pos):
                    withdraw_button.color = (10, 80, 180)
                elif cancel_button.isOver(pos):
                    cancel_button.color = (230, 230, 230)
                else:
                    deposit_button.color = (200, 20, 100)
                    withdraw_button.color = (20, 100, 200)
                    cancel_button.color = (255, 255, 255)

            #? open atm
                

        
        
        


                

                
        MoneyOnHand.show_text()    
        pygame.display.update()

main_menu = menu(1280, 720, "MAIN MENU", r"images\menu_background.png", shop_win_func)

main_menu.mainloop()



