import pygame

import settings
import variables


def ui_menu(screen, font: pygame.font.Font):
    back = pygame.Rect(25, 25, settings.WIDTH - 50, settings.HEIGHT - 50)
    pygame.draw.rect(screen, (200, 200, 200), back)
    top = 30
    left = 30
    screen.blit(
        font.render(settings.NAME, True, 'black'),
        (left, top))
    screen.blit(
        font.render('Управление:', True, 'black'),
        (left, top*3))
    # ЛИ
    screen.blit(
        font.render('Левый игрок (ЛИ):', True, 'black'),
        (left, top*5))
    screen.blit(
        font.render('A и D - движение влево и вправо', True, 'black'),
        (left*2, top*6))
    # ПИ
    screen.blit(
        font.render('Правый игрок (ПИ):', True, 'black'),
        (left, top*7))
    screen.blit(
        font.render('Стрелки < и > - движение влево и вправо', True, 'black'),
        (left*2, top*8))
    #
    screen.blit(
        font.render('Первый этап: Тренировка.', True, 'black'),
        (left, top*12))
    screen.blit(
        font.render('Чтобы начать, одновременно удерживайте W', True, 'black'),
        (left, top*14))
    screen.blit(
        font.render('и стрелку вверх (^)', True, 'black'),
        (left, top*15))
    screen.blit(
        font.render('Удерживайте красный шар на вершине горы', True, 'black'),
        (left, top*17))
    screen.blit(
        font.render('как можно дольше.', True, 'black'),
        (left, top*18))
    screen.blit(
        font.render('У вас 2 минуты.', True, 'black'),
        (left, top*19))


def ui_game(screen, font, minutes, seconds):
    pan = settings.WIDTH // 4
    if variables.wind_direction == 0:
        wind = '00000000000000000000'
    elif variables.wind_direction == 1:
        wind = '>>>>>>>>>>>>>>>>>>>>'
    elif variables.wind_direction == -1:
        wind = '<<<<<<<<<<<<<<<<<<<<'
    screen.blit(
            font.render(wind, True, 'black'),
            (settings.WIDTH // 2 - 120, settings.HEIGHT // 2 - 100),
        )
    out = '{minutes:02d}:{seconds:02d}'.format(minutes=minutes,
                                               seconds=seconds)
    screen.blit(
                font.render(out, True, 'black'),
                (pan, 160),
    )
    screen.blit(
                font.render(f'{variables.health}', True, 'black'),
                (settings.WIDTH - pan, 160),
    )


def ui_pre_exam(screen, font):
    back = pygame.Rect(25, 25, settings.WIDTH - 50, settings.HEIGHT - 50)
    pygame.draw.rect(screen, (200, 200, 200), back)
    top = 30
    left = 30
    screen.blit(
        font.render('Результаты тренировки:', True, 'black'),
        (left, top))
    screen.blit(
        font.render(f'Общее время тренировки - {variables.stage_time}',
                    True, 'black'),
        (left, top*3))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        font.render(f'Самый активный игрок (по времени) - {player}',
                    True, 'black'),
        (left, top*4))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        font.render(f'Самый активный игрок (по нажатиям) - {player}',
                    True, 'black'),
        (left, top*5))
    screen.blit(
        font.render(f'Общее время кооперации - {variables.cooperative_time}',
                    True, 'black'),
        (left, top*6))
    screen.blit(
        font.render(f'Общее время конфликта - {variables.conflict_time}',
                    True, 'black'),
        (left, top*7))
    screen.blit(
        font.render('Второй этап: Зачёт.', True, 'black'),
        (left, top*10))
    screen.blit(
        font.render('Чтобы начать, одновременно удерживайте W', True, 'black'),
        (left, top*12))
    screen.blit(
        font.render('и стрелку вверх (^)', True, 'black'),
        (left, top*13))
    screen.blit(
        font.render('Удерживайте красный шар на вершине горы', True, 'black'),
        (left, top*15))
    screen.blit(
        font.render('как можно дольше.', True, 'black'),
        (left, top*16))
    screen.blit(
        font.render('У вас 2 минуты.', True, 'black'),
        (left, top*17))


def ui_result(screen, font):
    back = pygame.Rect(25, 25, settings.WIDTH - 50, settings.HEIGHT - 50)
    pygame.draw.rect(screen, (200, 200, 200), back)
    top = 30
    left = 30
    screen.blit(
        font.render('Результаты зачёта:', True, 'black'),
        (left, top))
    screen.blit(
        font.render(f'Общее время тренировки - {variables.stage_time}',
                    True, 'black'),
        (left, top*3))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        font.render(f'Самый активный игрок (по времени) - {player}',
                    True, 'black'),
        (left, top*4))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        font.render(f'Самый активный игрок (по нажатиям) - {player}',
                    True, 'black'),
        (left, top*5))
    screen.blit(
        font.render(f'Общее время кооперации - {variables.cooperative_time}',
                    True, 'black'),
        (left, top*6))
    screen.blit(
        font.render(f'Общее время конфликта - {variables.conflict_time}',
                    True, 'black'),
        (left, top*7))
