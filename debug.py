import pygame


pygame.font.init()
font = pygame.font.SysFont('arial', 20)


def debug(value, info='None', y=60, x=40):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(f'{info}={value}', True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)
