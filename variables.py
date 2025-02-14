import pygame
from datetime import datetime as dt, timedelta as td

import settings


SESSION_STAGE = ''
# START_MENU, ABOUT, INPUT_DATA, GUIDE,
# START_TRAIN, PRE_EXAM, START_EXAM, STOP_STAGE, RESULT

SESSION_START = dt.now()
SESSION_END = dt.now()

ticks = pygame.time.get_ticks()
health = settings.health

ticks_current = 0
minutes = 0

wind_direction = 0
wind_strength = settings.wind_strength
wind_timer = 0

ad_freezed = False

is_warmuped = False
debug_activated = False

start_stage_time = dt.now()
stage_time = td()

lp_active_time = td()
lp_left_time = dt.now()
lp_right_time = dt.now()
lp_key_pushes = 0

rp_active_time = td()
rp_left_time = dt.now()
rp_right_time = dt.now()
rp_key_pushes = 0

conflict = False
conflict_started = False
conflict_time = td()
start_conflict_time = dt.now()

cooperation = False
coop_started = False
cooperative_time = td()
start_cooperative_time = dt.now()

active_p = ''
active_kpush_p = ''

pl_pos_log = False
