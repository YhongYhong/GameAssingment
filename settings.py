# game setup
WIDTH    = 1280	
HEIGHT   = 720
FPS      = 60
TILESIZE = 80
# Map setup
WIDTH_MAP = 3500
HEIGHT_MAP = 1000
# Player setup
WIDTH_PLAYER = 64
HEIGHT_PLAYER = 64

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 1280
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'Assets/Mainmenu/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons 
weapon_data = {
	# 'sword': {'cooldown': 100, 'damage': 15,'graphic':'Assets/weapons/sword/full.png'},
	'lance': {'cooldown': 300, 'damage': 30,'graphic':'Assets/weapons/lance/full.png'},
	'axe': {'cooldown': 400, 'damage': 40, 'graphic':'Assets/weapons/axe/full.png'},
	# 'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'Assets/weapons/rapier/full.png'},
	# 'sai':{'cooldown': 80, 'damage': 10, 'graphic':'Assets/weapons/sai/full.png'}
	}

# enemy
monster_data = {
	# 'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	# 'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	# 'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	# 'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300},
	'monkey': {'health': 100,'exp':120,'damage':6,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 1.5, 'resistance': 5, 'attack_radius': 50, 'notice_radius': 3500}}
