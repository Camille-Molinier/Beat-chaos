import pygame

class World:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            self.update()
            self.draw()

            # mettre à jour l'écran
            pygame.display.flip()
            # si le joueur ferme la fenêtre
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

    def update(self):
        pass

    def draw(self):
        pass