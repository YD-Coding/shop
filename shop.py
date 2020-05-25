import pygame
from atm import atm
from menu import menu
from player import Player
from menu import menu

pygame.init()

shop_run = False

main_menu = menu(1280, 720, "MAIN MENU", r"images\menu_background.png")
main_menu.mainloop()


def shop_win_func():
    global shop_run
    shop_run = True
    
    shop_image = pygame.image.load(r"images\shop.png")
    shop_win = pygame.display.set_mode((1280, 720))
    main_atm = atm(r"images\ATM.png", -15, 335)
    man = Player(450, 650, shop_win)
    #shop_win.blit(man.char, (man.x, man.y))
    while shop_run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
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

            #if event.type = pygame.MOUSEBUTTONDOWN:
                

        
        shop_win.blit(shop_image, (0,0))
        man.draw()
        shop_win.blit(main_atm.image, (main_atm.x, main_atm.y))
        
        pygame.display.update()

shop_win_func()



