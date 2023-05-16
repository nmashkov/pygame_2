import settings
from settings import dark_grey
import variables
from fonts import (title1, title2, base2)


def ui_menu(screen):
    top = 30
    left = 30
    screen.blit(
        title1.render(settings.NAME, True, dark_grey),
        (left, top))
    screen.blit(
        title2.render('Управление:', True, dark_grey),
        (left, top*3))
    # ЛИ
    screen.blit(
        title2.render('Левый игрок (ЛИ):', True, dark_grey),
        (left, top*5))
    screen.blit(
        base2.render('A и D - движение влево и вправо', True, dark_grey),
        (left*2, top*6))
    # ПИ
    screen.blit(
        title2.render('Правый игрок (ПИ):', True, dark_grey),
        (left, top*7))
    screen.blit(
        base2.render('LEFT и RIGHT - движение влево и вправо',
                     True, dark_grey),
        (left*2, top*8))
    #
    screen.blit(
        title2.render('Первый этап: Тренировка.', True, dark_grey),
        (left, top*12))
    screen.blit(
        base2.render('Чтобы начать, одновременно удерживайте W',
                     True, dark_grey),
        (left, top*14))
    screen.blit(
        base2.render('и стрелку вверх (UP)', True, dark_grey),
        (left, top*15))
    screen.blit(
        base2.render('Удерживайте красный шар на вершине горы',
                     True, dark_grey),
        (left, top*17))
    screen.blit(
        base2.render('как можно дольше.', True, dark_grey),
        (left, top*18))
    screen.blit(
        base2.render('У вас 2 минуты.', True, dark_grey),
        (left, top*19))


def ui_game(screen, minutes, seconds):
    pan = settings.WIDTH // 4
    if variables.wind_direction == 0:
        wind = '00000000000000000000'
    elif variables.wind_direction == 1:
        wind = '>>>>>>>>>>>>>>>>>>>>'
    elif variables.wind_direction == -1:
        wind = '<<<<<<<<<<<<<<<<<<<<'
    screen.blit(
            base2.render(wind, True, dark_grey),
            (settings.WIDTH // 2 - 120, settings.HEIGHT // 2 - 100),
        )
    out = '{minutes:02d}:{seconds:02d}'.format(minutes=minutes,
                                               seconds=seconds)
    screen.blit(
                base2.render(out, True, dark_grey),
                (pan, 160),
    )
    screen.blit(
                base2.render(f'{variables.health}', True, dark_grey),
                (settings.WIDTH - pan, 160),
    )


def ui_pre_exam(screen):
    top = 30
    left = 30
    screen.blit(
        title2.render('Результаты тренировки:', True, dark_grey),
        (left, top))
    screen.blit(
        base2.render(f'Общее время тренировки - {variables.stage_time}',
                     True, dark_grey),
        (left, top*3))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        base2.render(f'Самый активный игрок (по времени) - {player}',
                     True, dark_grey),
        (left, top*4))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        base2.render(f'Самый активный игрок (по нажатиям) - {player}',
                     True, dark_grey),
        (left, top*5))
    screen.blit(
        base2.render(f'Общее время кооперации - {variables.cooperative_time}',
                     True, dark_grey),
        (left, top*6))
    screen.blit(
        base2.render(f'Общее время конфликта - {variables.conflict_time}',
                     True, dark_grey),
        (left, top*7))
    screen.blit(
        title2.render('Второй этап: Зачёт.', True, dark_grey),
        (left, top*10))
    screen.blit(
        base2.render('Чтобы начать, одновременно удерживайте W',
                     True, dark_grey),
        (left, top*12))
    screen.blit(
        base2.render('и стрелку вверх (UP)', True, dark_grey),
        (left, top*13))
    screen.blit(
        base2.render('У вас 2 минуты.', True, dark_grey),
        (left, top*15))


def ui_result(screen):
    top = 30
    left = 30
    screen.blit(
        title2.render('Результаты зачёта:', True, dark_grey),
        (left, top))
    screen.blit(
        base2.render(f'Общее время зачёта - {variables.stage_time}',
                     True, dark_grey),
        (left, top*3))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        base2.render(f'Самый активный игрок (по времени) - {player}',
                     True, dark_grey),
        (left, top*4))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        base2.render(f'Самый активный игрок (по нажатиям) - {player}',
                     True, dark_grey),
        (left, top*5))
    screen.blit(
        base2.render(f'Общее время кооперации - {variables.cooperative_time}',
                     True, dark_grey),
        (left, top*6))
    screen.blit(
        base2.render(f'Общее время конфликта - {variables.conflict_time}',
                     True, dark_grey),
        (left, top*7))
    screen.blit(
        base2.render(f'Количество очков - {variables.health}',
                     True, dark_grey),
        (left, top*8))
