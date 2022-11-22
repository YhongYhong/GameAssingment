import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from weapon import Weapon
from ui import UI
from enemy import Enemy
from pause import Pause
from item import Item
import random

SCREEN = pygame.display.set_mode((1280, 720))
font = pygame.font.Font('Assets/Mainmenu/font/font.ttf',32)

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()
		self.game_paused = False

		# sprite group setup
		self.visible_sprites = YsortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.visible_item = pygame.sprite.Group()

		# attack sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()
		self.player_alive = True

		# sprite setup
		self.create_player()

		# user interface
		self.ui = UI()
		self.pause = Pause()

		# spawn
		self.enemy_group = pygame.sprite.Group()
		self.spawn = 0

		# score
		self.point = 0

		# item
		self.itemgroup = pygame.sprite.Group()

	def create_player(self):
		self.player = Player((1750,500),[self.visible_sprites],self.obstacle_sprites,self.create_attack,self.destroy_attack)
		# spawn enemy setting
		# self.enemy_number = 1
		# while self.enemy_number <= 1:
		# 		enemy_x = random.randint(WIDTH_PLAYER,(WIDTH_MAP-WIDTH_PLAYER))
		# 		enemy_y = random.randint(HEIGHT_PLAYER,(HEIGHT_MAP-HEIGHT_PLAYER))
		# 		self.enemy = Enemy(
		# 							'monkey',
		# 							(enemy_x,enemy_y),
		# 							[self.visible_sprites,self.attackable_sprites],
		# 							self.obstacle_sprites,
		# 							self.damage_player)
		# 		self.enemy_number += 1

	def create_attack(self):
		self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
				if collision_sprites:
					for target_sprite in collision_sprites:
						target_sprite.get_damage(self.player,attack_sprite.sprite_type)

		if self.visible_item:
			for item in self.visible_item:
				if pygame.sprite.collide_rect(item,self.player):
					self.player.health += 10
					if self.player.health > 100:
						self.player.health = 100
					item.kill()

	def damage_player(self,amount):
		if self.player.vulnerable:
			self.player.health -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			# spawn particles

	def enemy_spawn(self):
		self.spawn_rate = 150
		self.spawn = random.randint(10,self.spawn_rate)
		enemy_x = random.randint(WIDTH_PLAYER,(WIDTH_MAP-WIDTH_PLAYER))
		enemy_y = random.randint(HEIGHT_PLAYER,(HEIGHT_MAP-HEIGHT_PLAYER))
		if self.spawn == 10 or self.spawn == 11:
			new_enemy = Enemy('monkey',
								(enemy_x,enemy_y),
								[self.visible_sprites,self.attackable_sprites],
								self.obstacle_sprites,
								self.damage_player,
								self.trigger_death_particles,self)
			self.enemy_group.add(new_enemy)

	def toggle_menu(self):
		self.game_paused = not self.game_paused

	def check_player_death(self):
		if self.player.health <= 0:
			self.player_alive = False

	def force_death(self):
		self.player_alive = False

	def trigger_death_particles(self,particle_type): # when enemies dead
		monster_data[particle_type]['health'] += 2
		monster_data[particle_type]['speed'] += 0.03
		self.point += 50
		self.player.speed += 0.05

	def show_score(self):
		text_surf = font.render('Score : ' + str(self.point), True, (255,255,255))
		text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0] - 230, self.display_surface.get_size()[1] - 30))

		pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
		SCREEN.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.ui.display(self.player)
		self.check_player_death()
		self.show_score()

		if self.game_paused:
			pause = Pause()
			pause.pause_menu()
			
		else:
			self.visible_sprites.update()
			self.visible_sprites.enemy_updates(self.player)
			self.player_attack_logic()
			# spawn enemy
			self.enemy_spawn()
			self.enemy_group.update()

class YsortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('Assets/Maps2.png').convert()
		self.floor_surf = pygame.transform.scale(self.floor_surf,(WIDTH_MAP,HEIGHT_MAP))
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):

		# getting the offset
		if player.rect.centerx > (WIDTH/2) and player.rect.centerx < (WIDTH_MAP - (WIDTH/2)):		# setting to make camera locked when player is in the brim map
			self.offset.x = player.rect.centerx - self.half_width
		if player.rect.centery > (HEIGHT/2) and player.rect.centery < (HEIGHT_MAP - (HEIGHT/2)):	# setting to make camera locked when player is in the brim map
			self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):	# draw all sprite such as the player , enemy
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
			
	def enemy_updates(self,player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy'] # draw enemies chasing the player
		for enemy in enemy_sprites:	
			enemy.enemy_update(player)