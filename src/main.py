import pygame
pygame.init()

#générer la fenêtre

pygame.display.set_caption("Chaos")
screen = pygame.display.set_mode((1080, 720))

#chargement de l'arrière plan

background = pygame.image.load('assets/fond chaos.PNG')

running = True

# boucle du jeu

while running :

    #appliquer l'arrière plan
    screen.blit(background, (-50, 50))

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme la fenêtre
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()