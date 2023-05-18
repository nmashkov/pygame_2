import pygame
from datetime import datetime as dt

import settings
from settings import dark_grey, accent
import variables
from fonts import (title1, title2, base, base2)


def ui_credits(screen):
    top = 30
    left = 70
    center = settings.WIDTH // 2
    #
    screen.blit(title1.render(settings.NAME, True, dark_grey),
                (center - 66, top))
    screen.blit(base2.render('Идея', True, dark_grey),
                (left, top*4))
    text = base2.render('Малишевский А.В.', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*4))
    screen.blit(base2.render('Разработка', True, dark_grey),
                (left, top*5.5))
    text = base2.render('Машков Н.А.', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*5.5))
    screen.blit(base2.render('Дизайн', True, dark_grey),
                (left, top*7))
    text = base2.render('Мануйленко Е.В.', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*7))
    #
    text = base2.render('СПбГУ ГА', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH // 2 - text.get_width()*.5, top*11))
    text = base.render('2023', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH // 2 - text.get_width()*.5, top*12))


def ui_menu(screen):
    top = 30
    left = 70
    center = settings.WIDTH // 2
    #
    screen.blit(title1.render(settings.NAME, True, dark_grey),
                (center - 66, top))
    screen.blit(title2.render('Управление', True, dark_grey),
                (center - 70, top*3.5))
    # ЛИ
    screen.blit(base2.render('Левый игрок (ЛИ)', True, dark_grey),  # 175
                (left, top*5.5))
    button = pygame.Rect(left + 175*.2 - 20, top*7.5-8, 40, 40)
    pygame.draw.rect(screen, accent, button)
    button = pygame.Rect(left + 175*.2 - 18, top*7.5-6, 36, 36)
    pygame.draw.rect(screen, settings.bg_color, button)
    button = pygame.Rect(left + 175*.8 - 20, top*7.5-8, 40, 40)
    pygame.draw.rect(screen, accent, button)
    button = pygame.Rect(left + 175*.8 - 18, top*7.5-6, 36, 36)
    pygame.draw.rect(screen, settings.bg_color, button)
    screen.blit(base2.render('A', True, dark_grey),  # 14
                (left + 175*.2 - 7, top*7.5))
    screen.blit(base2.render('D', True, dark_grey),  # 14
                (left + 175*.8 - 7, top*7.5))
    screen.blit(base.render('Движение влево и вправо', True, dark_grey),
                (left + (175 - 205)*.5, top*9))
    # ПИ
    screen.blit(base2.render('Правый игрок (ПИ)', True, dark_grey),  # 188
                (settings.WIDTH - left - 188, top*5.5))
    button = pygame.Rect(settings.WIDTH-left-188*.8-37, top*7.5-8, 74, 40)
    pygame.draw.rect(screen, accent, button)
    button = pygame.Rect(settings.WIDTH-left-188*.8-35, top*7.5-6, 70, 36)
    pygame.draw.rect(screen, settings.bg_color, button)
    button = pygame.Rect(settings.WIDTH-left-188*.2-43, top*7.5-8, 86, 40)
    pygame.draw.rect(screen, accent, button)
    button = pygame.Rect(settings.WIDTH-left-188*.2-41, top*7.5-6, 82, 36)
    pygame.draw.rect(screen, settings.bg_color, button)
    screen.blit(base2.render('LEFT', True, dark_grey),  # 48
                (settings.WIDTH - left - 188*.8 - 24, top*7.5))
    screen.blit(base2.render('RIGHT', True, dark_grey),  # 61
                (settings.WIDTH - left - 188*.2 - 30, top*7.5))
    screen.blit(base.render('Движение влево и вправо', True, dark_grey),  # 205
                (settings.WIDTH - left - (205 + 188)*.5, top*9))
    #
    screen.blit(base2.render('Первый этап', True, dark_grey),  # 125
                (left + (175 - 125)*.5, top*11))
    screen.blit(base.render('Тренировка', True, dark_grey),  # 94
                (left + (175 - 94)*.5, top*12))
    #
    screen.blit(base2.render('Время', True, dark_grey),  # 63
                (settings.WIDTH - left - (63 + 188)*.5, top*11))
    screen.blit(base.render('1 минута', True, dark_grey),  # 69
                (settings.WIDTH - left - (69 + 188)*.5, top*12))
    #
    button = pygame.Rect(center-263, top*14-10, 526, 40)
    pygame.draw.rect(screen, accent, button)
    button = pygame.Rect(center-261, top*14-8, 522, 36)
    pygame.draw.rect(screen, settings.bg_color, button)
    screen.blit(base.render('Чтобы начать, одновременно нажмите W и '
                            'стрелку вверх (UP)', True, dark_grey),
                (center - 251, top*14))
    screen.blit(base.render('Удерживайте красный шар на вершине '
                            'горы как можно дольше', True, dark_grey),
                (center - 258, top*15.5))
    #
    date = dt.now()
    if len(str(date.minute)) > 1:
        minutes = date.minute
    else:
        minutes = f'0{date.minute}'
    text = base.render(f'{date.hour}:{minutes}-'
                       f'{str(settings.SESSION_DIR)[:8]}',
                       True, dark_grey)
    screen.blit(text, (center - text.get_width()*.5,
                       settings.HEIGHT - text.get_height()))


def ui_game(screen, minutes, seconds):
    hud = pygame.Rect(21, 20, settings.WIDTH-20*2-1, 40)
    pygame.draw.rect(screen, (255, 255, 255), hud)
    pan = settings.WIDTH // 4
    center = settings.WIDTH // 2
    # hud
    out = f'{minutes:02d}:{seconds:02d}'
    screen.blit(base2.render(out, True, dark_grey),
                (pan - 29, 30))
    screen.blit(base2.render(f'Попытки: {variables.health}', True, dark_grey),
                (settings.WIDTH - pan - 56, 30))
    # wind
    if variables.wind_direction == 0:
        wind = '00000000000000000000'
    elif variables.wind_direction == 1:
        wind = '>>>>>>>>>>>>>>>>>>>>'
    elif variables.wind_direction == -1:
        wind = '<<<<<<<<<<<<<<<<<<<<'
    screen.blit(base2.render(wind, True, dark_grey),
                (center - 130, settings.HEIGHT // 2 - 100))


def ui_pre_exam(screen):
    top = 30
    left = 30
    center = settings.WIDTH // 2
    #
    screen.blit(title1.render('Результаты тренировки', True, dark_grey),  # 481
                (center - 481*.5, top))
    #
    screen.blit(base2.render('Общее время тренировки', True, dark_grey),  # 256
                (left, top*4))
    text = base2.render(f'{variables.stage_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*4))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(base2.render('Самый активный игрок (по времени)',
                             True, dark_grey),
                (left, top*5))
    screen.blit(base2.render(f'{player}', True, dark_grey),  # 29
                (settings.WIDTH - left - 29, top*5))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(base2.render('Самый активный игрок (по нажатиям)',
                             True, dark_grey),
                (left, top*6))
    screen.blit(base2.render(f'{player}', True, dark_grey),
                (settings.WIDTH - left - 29, top*6))
    screen.blit(base2.render('Общее время кооперации', True, dark_grey),
                (left, top*7))
    text = base2.render(f'{variables.cooperative_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*7))
    screen.blit(base2.render('Общее время конфликта', True, dark_grey),
                (left, top*8))
    text = base2.render(f'{variables.conflict_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*8))
    screen.blit(base2.render('Количество очков', True, dark_grey),
                (left, top*9))
    screen.blit(base2.render(f'{variables.health}', True, dark_grey),
                (settings.WIDTH - left - 13, top*9))
    #
    left = 70
    screen.blit(base2.render('Второй этап', True, dark_grey),  # 120
                (left + (175 - 120)*.5, top*12))
    screen.blit(base.render('Зачёт', True, dark_grey),  # 45
                (left + (175 - 45)*.5, top*13))
    #
    screen.blit(base2.render('Время', True, dark_grey),  # 63
                (settings.WIDTH - left - (63 + 188)*.5, top*12))
    t = base.render('2 минуты', True, dark_grey)
    screen.blit(t, (settings.WIDTH - left - (t.get_width() + 188)*.5, top*13))
    #
    button = pygame.Rect(center-263, top*17-10, 526, 40)
    pygame.draw.rect(screen, accent, button)
    button = pygame.Rect(center-261, top*17-8, 522, 36)
    pygame.draw.rect(screen, settings.bg_color, button)
    screen.blit(base.render('Чтобы начать, одновременно нажмите W и '
                            'стрелку вверх (UP)', True, dark_grey),
                (center - 251, top*17))
    #
    date = dt.now()
    if len(str(date.minute)) > 1:
        minutes = date.minute
    else:
        minutes = f'0{date.minute}'
    text = base.render(f'{date.hour}:{minutes}-'
                       f'{str(settings.SESSION_DIR)[:8]}',
                       True, dark_grey)
    screen.blit(text, (center - text.get_width()*.5,
                       settings.HEIGHT - text.get_height()))


def ui_result(screen):
    top = 30
    left = 30
    center = settings.WIDTH // 2
    #
    screen.blit(title1.render('Результаты зачёта', True, dark_grey),  # 377
                (center - 377*.5, top))
    #
    screen.blit(base2.render('Общее время зачёта', True, dark_grey),
                (left, top*4))
    text = base2.render(f'{variables.stage_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*4))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(base2.render('Самый активный игрок (по времени)',
                             True, dark_grey),
                (left, top*5))
    screen.blit(base2.render(f'{player}', True, dark_grey),  # 29
                (settings.WIDTH - left - 29, top*5))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(base2.render('Самый активный игрок (по нажатиям)',
                             True, dark_grey),
                (left, top*6))
    screen.blit(base2.render(f'{player}', True, dark_grey),
                (settings.WIDTH - left - 29, top*6))
    screen.blit(base2.render('Общее время кооперации', True, dark_grey),
                (left, top*7))
    text = base2.render(f'{variables.cooperative_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*7))
    screen.blit(base2.render('Общее время конфликта', True, dark_grey),
                (left, top*8))
    text = base2.render(f'{variables.conflict_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*8))
    screen.blit(base2.render('Количество очков', True, dark_grey),
                (left, top*9))
    screen.blit(base2.render(f'{variables.health}', True, dark_grey),
                (settings.WIDTH - left - 13, top*9))
    #
    button = pygame.Rect(center-151, top*17-10, 302, 40)
    pygame.draw.rect(screen, accent, button)
    button = pygame.Rect(center-149, top*17-8, 298, 36)
    pygame.draw.rect(screen, settings.bg_color, button)
    screen.blit(base.render('Чтобы завершить, нажмите ENTER', True, dark_grey),
                (center - 276*.5, top*17))  # 276
    #
    date = dt.now()
    if len(str(date.minute)) > 1:
        minutes = date.minute
    else:
        minutes = f'0{date.minute}'
    text = base.render(f'{date.hour}:{minutes}-'
                       f'{str(settings.SESSION_DIR)[:8]}',
                       True, dark_grey)
    screen.blit(text, (center - text.get_width()*.5,
                       settings.HEIGHT - text.get_height()))
    # text = base.render('Чтобы завершить, нажмите ENTER', True, dark_grey)
    # print(f'w={text.get_width()}')
    # print(f'h={text.get_height()}')
