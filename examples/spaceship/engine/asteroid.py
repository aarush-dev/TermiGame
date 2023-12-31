import TermiGame, random, time

class Asteroid(TermiGame.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.init_health = 3
		self.health = self.init_health
		
	def reset(self):
		self.health = self.init_health
		self.unrender()
		self.y = random.randrange(-self.height - 40, -self.height)
		self.x = random.randrange(1, self.window.width - 1 - self.width)

	def check_bounds(self):
		if self.y > self.window.height:
			self.reset()

		if self.is_collided_with(self.window.player) and self.window.player.state == "alive":
			self.window.player.state = "dead"

		collided_bullet = self.check_group_collision(self.window.player.bullets)
		if collided_bullet:
			self.health -= 1
			if self.health == 0:
				TermiGame.sprite.Sprite(window=self.window, x=self.x, y=self.y, direction=(0, 0), speed=(0, 0), images=self.window.explosion_imgs, image_num=0, color_pair=((255, 255, 0), None), group=self.window.explosions)
				self.reset()
			collided_bullet.unrender()
			self.window.player.bullets.remove(collided_bullet)


