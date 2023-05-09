import datetime as dt

import settings


SESSION_STAGE = ''
# START_MENU, START_TRAIN, PRE_EXAM, START_EXAM, STOP_STAGE, RESULT

health = settings.health
wind_direction = 0
wind_direction_prev = 0
wind_strength = settings.wind_strength
wind_timer = 0
is_warmuped = False

start_stage_time = dt.datetime.now()
stage_time = dt.timedelta()

lp_active_time = dt.timedelta()
lp_left_time = dt.datetime.now()
lp_right_time = dt.datetime.now()
lp_key_pushes = 0

rp_active_time = dt.timedelta()
rp_left_time = dt.datetime.now()
rp_right_time = dt.datetime.now()
rp_key_pushes = 0

conflict = False
conflict_started = False
conflict_time = dt.timedelta()
start_conflict_time = dt.datetime.now()

cooperation = False
coop_started = False
cooperative_time = dt.timedelta()
start_cooperative_time = dt.datetime.now()

active_p = ''
active_kpush_p = ''

pl_pos_log = False
