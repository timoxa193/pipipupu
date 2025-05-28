from pygame import*
font.init()
window = display.set_mode((1400,900))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.jpg'), (1400,900))
sprite2 = transform.scale(image.load('sprite2.png'),(100,100))

clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.rect = self.image.get_rect()   
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed   

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):    
        if key_pressed[K_s] and self.rect.y < 840:
            self.rect.y+=10
        if key_pressed[K_w]and self.rect.y > 1:
            self.rect.y-=10
        if key_pressed[K_d] and self.rect.x < 1340:
            self.rect.x+=10
        if key_pressed[K_a]and self.rect.x > 1:
            self.rect.x-=10

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 1015:
            self.direction = 'right'
        if self.rect.x >= 1315:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed 

class Wall(sprite.Sprite):
    def __init__(self, wight, hight, x, y):
        super().__init__()
        self.wight = wight
        self.hight = hight
        self.image = Surface((self.wight, self.hight))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((0, 185, 0))

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

wall1 = Wall(770, 15, 250, 20)
wall2 = Wall(15, 700, 250, 150)       
wall3 = Wall(15, 700, 400, 20)
wall4 = Wall(770, 15, 250, 850)
wall5 = Wall(15, 700, 550, 150)
wall6 = Wall(15, 300, 700, 20)
wall7 = Wall(15, 400, 700, 450)
wall8 = Wall(15, 650, 850, 200)
wall9 = Wall(15, 740, 1005, 110) 
steny = [wall1,wall2, wall3, wall4, wall5, wall6, wall7 ,wall8, wall9]

player = Player('hero.png', 100, 100, 10)
enemy = Enemy('cyborg.png', 1000, 500, 10)
gold = GameSprite('treasure.png', 1200, 750, 0)
game=True
finish = False
fond = font.Font(None, 70)
win = fond.render('U WIN', True, (0, 175, 0 ))
lose = fond.render('U LOSE', True, (255, 0, 0 ))
while game:
    if finish == False:
        key_pressed = key.get_pressed()
        window.blit(background, (0,0))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        gold.update()
        gold.reset()
        for stena in steny:
            stena.draw_wall()
            if sprite.collide_rect(player, stena):
                window.blit(lose, (200, 200))
                finish = True
        if sprite.collide_rect(player, gold):
            window.blit(win, (200, 200))
            finish = True
        if sprite.collide_rect(player, enemy):
            window.blit(lose, (200,200))
            finish = True
    for evnt in event.get():
        if evnt.type == QUIT:
            game=False
    display.update()
    clock.tick(60)
    
