import pygame
from pygame.locals import *
import sys
import random

pygame.init()
vec = pygame.math.Vector2
Width = 1000
Hight = 800
screen = pygame.display.set_mode((Width,Hight))
done = False
has_hit_ground_p1 = True
has_hit_ground_p2 = True
P1_STRUCK_DOWN = False
P2_STRUCK_DOWN = False
no_colls_p2 = True
Acc = 0.3
Fric = -0.09
frames = 0
P1_Iframes = 0
P2_Iframes = 0
P1_HP = 3
P2_HP = 3
global plooking_at
plooking_at_p1 = "Right"
looked_at_bullet = "Right"
plooking_at_p2 = "Left"
#Images (in a for loop to minimize)
for i in range(1):
    #player 1

    #idle
    player_F1 = pygame.image.load(
        "Idle_AnimationF1.png").convert_alpha()
    player_F1 = pygame.transform.scale(player_F1, (70, 70))
    player_F1_mirrored = pygame.transform.flip(player_F1, True, False)

    player_F2 = pygame.image.load(
        "Idle_AnimationF2.png").convert_alpha()
    player_F2 = pygame.transform.scale(player_F2, (70, 70))
    player_F2_mirrored = pygame.transform.flip(player_F2, True, False)

    player_F3 = pygame.image.load(
        "Idle_AnimationF3.png").convert_alpha()
    player_F3 = pygame.transform.scale(player_F3, (70, 70))
    player_F3_mirrored = pygame.transform.flip(player_F3, True, False)

    player_F4 = pygame.image.load(
        "Idle_AnimationF4.png").convert_alpha()
    player_F4 = pygame.transform.scale(player_F4, (70, 70))
    player_F4_mirrored = pygame.transform.flip(player_F4, True, False)

    p1_idle_animation = [player_F1,player_F2,player_F3,player_F4]
    p1_idle_animation_mirorred = [player_F1_mirrored,player_F2_mirrored,player_F3_mirrored,player_F4_mirrored]

    #hurt

    player_Hit_F1 = pygame.image.load("P1_Hit_F1.png").convert_alpha()
    player_Hit_F1 = pygame.transform.scale(player_Hit_F1, (70, 70))
    player_Hit_F1_mirrored = pygame.transform.flip(player_Hit_F1, True, False)

    player_Hit_F2 = pygame.image.load("P1_Hit_F2.png").convert_alpha()
    player_Hit_F2 = pygame.transform.scale(player_Hit_F2, (70, 70))
    player_Hit_F2_mirrored = pygame.transform.flip(player_Hit_F2, True, False)

    player_Hit_F3 = pygame.image.load("P1_Hit_F3.png").convert_alpha()
    player_Hit_F3 = pygame.transform.scale(player_Hit_F3, (70, 70))
    player_Hit_F3_mirrored = pygame.transform.flip(player_Hit_F3, True, False)

    player_Hit_F4 = pygame.image.load("P1_Hit_F3.png").convert_alpha()
    player_Hit_F4 = pygame.transform.scale(player_Hit_F4, (70, 70))
    player_Hit_F4_mirrored = pygame.transform.flip(player_Hit_F4, True, False)

    p1_hurt_animation = [player_Hit_F1,player_Hit_F2,player_Hit_F3,player_Hit_F4]
    p1_hurt_animation_mirrored = [player_Hit_F1_mirrored,player_Hit_F2_mirrored,player_Hit_F3_mirrored,player_Hit_F4_mirrored]

    #HP Bar

    player1_HP_Bar_3 = pygame.image.load("P1_HP_3.png").convert_alpha()
    player1_HP_Bar_3 = pygame.transform.scale(player1_HP_Bar_3 , (124, 64))

    player1_HP_Bar_2 = pygame.image.load("P1_HP_2.png").convert_alpha()
    player1_HP_Bar_2 = pygame.transform.scale(player1_HP_Bar_2 , (124, 64))

    player1_HP_Bar_1 = pygame.image.load("P1_HP_1.png").convert_alpha()
    player1_HP_Bar_1 = pygame.transform.scale(player1_HP_Bar_1 , (124, 64))

    player1_HP_Bar_0 = pygame.image.load("P1_HP_0.png").convert_alpha()
    player1_HP_Bar_0 = pygame.transform.scale(player1_HP_Bar_0 , (124, 64))

    player_image1 = player_F1
    #player 2

    #idle
    player2_F1 = pygame.image.load("P2_Idle_F1.png").convert_alpha()
    player2_F1 = pygame.transform.scale(player2_F1, (70, 70))
    player2_F1_mirrored = pygame.transform.flip(player2_F1, True, False)

    player2_F2 = pygame.image.load("P2_Idle_F2.png").convert_alpha()
    player2_F2 = pygame.transform.scale(player2_F2, (70, 70))
    player2_F2_mirrored = pygame.transform.flip(player2_F2, True, False)

    player2_F3 = pygame.image.load("P2_Idle_F3.png").convert_alpha()
    player2_F3 = pygame.transform.scale(player2_F3, (70, 70))
    player2_F3_mirrored = pygame.transform.flip(player2_F3, True, False)

    player2_F4 = pygame.image.load("P2_Idle_F4.png").convert_alpha()
    player2_F4 = pygame.transform.scale(player2_F4, (70, 70))
    player2_F4_mirrored = pygame.transform.flip(player2_F4, True, False)

    player2_animation = [player2_F1, player2_F2, player2_F3, player2_F4]
    player2_animation_mirrored = [player2_F1_mirrored, player2_F2_mirrored, player2_F3_mirrored, player2_F4_mirrored]
    player_image2 = player2_F1


    #hurt

    player2_Hit_F1 = pygame.image.load("P2_hurt_F1.png").convert_alpha()
    player2_Hit_F1 = pygame.transform.scale(player2_Hit_F1, (70, 70))
    player2_Hit_F1_mirrored = pygame.transform.flip(player2_Hit_F1, True, False)

    player2_Hit_F2 = pygame.image.load("P2_hurt_F2.png").convert_alpha()
    player2_Hit_F2 = pygame.transform.scale(player2_Hit_F2, (70, 70))
    player2_Hit_F2_mirrored = pygame.transform.flip(player2_Hit_F2, True, False)

    player2_Hit_F3 = pygame.image.load("P2_hurt_F3.png").convert_alpha()
    player2_Hit_F3 = pygame.transform.scale(player2_Hit_F3, (70, 70))
    player2_Hit_F3_mirrored = pygame.transform.flip(player2_Hit_F3, True, False)

    player2_Hit_F4 = pygame.image.load("P2_Idle_F4.png").convert_alpha()
    player2_Hit_F4 = pygame.transform.scale(player2_Hit_F4, (70, 70))
    player2_Hit_F4_mirrored = pygame.transform.flip(player2_Hit_F4, True, False)

    p2_hurt_animation = [player2_Hit_F1,player2_Hit_F2,player2_Hit_F3,player2_Hit_F4]
    p2_hurt_animation_mirrored = [player2_Hit_F1_mirrored,player2_Hit_F2_mirrored,player2_Hit_F3_mirrored,player2_Hit_F4_mirrored]


    #HP bar

    player2_HP_Bar_3 = pygame.image.load(
        "P2_health_bar_3.png").convert_alpha()
    player2_HP_Bar_3 = pygame.transform.scale(player2_HP_Bar_3 , (124, 64))

    player2_HP_Bar_2 = pygame.image.load(
        "P2_health_bar_2.png").convert_alpha()
    player2_HP_Bar_2 = pygame.transform.scale(player2_HP_Bar_2 , (124, 64))

    player2_HP_Bar_1 = pygame.image.load(
        "P2_health_bar_1.png").convert_alpha()
    player2_HP_Bar_1 = pygame.transform.scale(player2_HP_Bar_1 , (124, 64))

    player2_HP_Bar_0 = pygame.image.load(
        "P2_health_bar_0.png").convert_alpha()
    player2_HP_Bar_0 = pygame.transform.scale(player2_HP_Bar_0 , (124, 64))



    #water drop
    water_drop_F1 = pygame.image.load(
        "Water_Drop_F1.png").convert_alpha()
    water_drop_F1 = pygame.transform.scale(water_drop_F1, (50, 50))
    water_drop_F1_mirrored = pygame.transform.flip(water_drop_F1, True, False)

    water_drop_F2 = pygame.image.load(
        "Water_Drop_F2.png").convert_alpha()
    water_drop_F2 = pygame.transform.scale(water_drop_F2, (50, 50))
    water_drop_F2_mirrored = pygame.transform.flip(water_drop_F2, True, False)

    water_drop_F3 = pygame.image.load(
        "Water_Drop_F3.png").convert_alpha()
    water_drop_F3 = pygame.transform.scale(water_drop_F3, (50, 50))
    water_drop_F3_mirrored = pygame.transform.flip(water_drop_F3, True, False)

    water_drop_F4 = pygame.image.load(
        "Water_Drop_F4.png").convert_alpha()
    water_drop_F4 = pygame.transform.scale(water_drop_F4, (50, 50))
    water_drop_F4_mirrored = pygame.transform.flip(water_drop_F4, True, False)


    water_drop_movement = [water_drop_F1,water_drop_F2,water_drop_F3,water_drop_F4]
    water_drop_movement_mirrored = [water_drop_F1_mirrored,water_drop_F2_mirrored,water_drop_F3_mirrored,water_drop_F4_mirrored]
    water_drop_image = water_drop_F1

    #platform / BG

    platform_image= pygame.image.load("Platform.png").convert_alpha()
    platform_image = pygame.transform.scale(platform_image, (250,20))

    #Reset stuffz

    blcolor = (0,0,0)
    bigfont = pygame.font.SysFont('Calibri',50)
    smallfont = pygame.font.SysFont('Calibri',30)

    lost_player_1 = bigfont.render('PLAYER 2 WON' , True , blcolor )

    lost_player_2 = bigfont.render('PLAYER 1 WON' , True , blcolor )

    lost_info = smallfont.render('Press R to restart' , True , blcolor )
    lost_info_textbox =lost_info.get_rect()

    lost_player_textbox = lost_player_1.get_rect()
    lost_info_textbox.center = (500,330)


clock = pygame.time.Clock()
has_hit_ground = True
class Player1(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.surf = player_image1
            self.rect = self.surf.get_rect()
            self.vel = vec(0 , 0)
            self.acc = vec(0 , 0)
            self.pos = vec((100 , 250))
    def respawn(self):
        self.surf = player_image1
        self.rect = self.surf.get_rect()
        self.vel = vec(0 , 0)
        self.acc = vec(0 , 0)
        self.pos = vec((100 , 250))
    def collisions(self):
        global P1_Iframes,P1_HP,P1_STRUCK_DOWN,collision_p1,no_colls_p1
        collision_p1 = pygame.sprite.spritecollide(player1, platforms, False,)
        if collision_p1 and collision_p1[0].rect.bottom > self.rect.bottom - 10 and no_colls_p1:
            global has_hit_ground_p1
            self.pos.y =collision_p1[0].rect.y + 1
            self.vel.y = 0
            has_hit_ground_p1 = True
        hit_by_bulletp1 = pygame.sprite.spritecollide(player1,Bullet_from_player_2 , False,)
        if hit_by_bulletp1 and P1_Iframes == 0 :
            P1_STRUCK_DOWN = True
            P1_Iframes += 200
    def under_platform(self):
        global no_colls_p1
        no_colls_p1= False
    def movement(self):
        self.surf = player_image1
        self.acc = vec(0 , 0.5)
        global plooking_at_p1
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a]:
            self.acc.x = -Acc
            plooking_at_p1 = "Left"
        elif pressed_keys[K_d]:
            self.acc.x = Acc
            plooking_at_p1 = "Right"

        #maths
        self.acc.x += self.vel.x * Fric
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        #loop around

        if self.pos.x > Width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = Width
    def jumping(self):
        self.vel.y = -15
class Player2(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.surf = player_image2
            self.rect = self.surf.get_rect()
            self.vel = vec(0 , 0)
            self.acc = vec(0 , 0)
            self.pos = vec((900 , 250))
    def respawn(self):
        self.surf = player_image2
        self.rect = self.surf.get_rect()
        self.vel = vec(0 , 0)
        self.acc = vec(0 , 0)
        self.pos = vec((900 , 250))
    def collisions(self):
        global  P2_HP,P2_Iframes,P2_STRUCK_DOWN,no_colls_p2
        hitsp2 = pygame.sprite.spritecollide(player2, platforms, False,)
        if hitsp2 and no_colls_p2 :
            global has_hit_ground_p2
            self.pos.y = hitsp2[0].rect.top +1
            self.vel.y = 0
            has_hit_ground_p2 = True
        hit_by_bulletp2 = pygame.sprite.spritecollide(player2,Bullet_from_player_1 , False,)
        if hit_by_bulletp2 and P2_Iframes == 0 :
            P2_STRUCK_DOWN = True
            P2_Iframes += 200
    def under_platform(self):
        global no_colls_p2
        no_colls_p2= False
    def movement(self):
        self.surf = player_image2
        self.acc = vec(0 , 0.5)
        global plooking_at_p2
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -Acc
            plooking_at_p2 = "Left"
        elif pressed_keys[K_RIGHT]:
            self.acc.x = Acc
            plooking_at_p2 = "Right"

        #maths
        self.acc.x += self.vel.x * Fric
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        #loop around

        if self.pos.x > Width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = Width
    def jumping(self):
        self.vel.y = -15
class BulletP1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = water_drop_image
        self.rect = self.surf.get_rect()
        self.go_right = False
        self.go_left = False
    def spawn(self,player1):
        global plooking_at_p1
        self.x = player1.pos.x
        self.y = player1.pos.y - 50
        self.rect.midbottom = self.x, self.y
        if plooking_at_p1 == "Left":
            self.go_left = True
            self.go_right = False
        if plooking_at_p1 == "Right":
            self.go_left = False
            self.go_right = True
    def moving(self):
        global p1_ammo_reservs
        self.surf = water_drop_image
        if self.go_right == True:
            self.x += 5
            self.rect.midbottom = self.x , self.y
            screen.blit(self.surf , (self.x , self.y))
            if self.x > Width:
                self.x =500
                self.y = 10000000
                self.go_left = False
                p1_ammo_reservs += 1
        elif self.go_left == True:
            self.x -= 5
            self.rect.midbottom = self.x , self.y
            screen.blit(self.surf, (self.x , self.y))
            if self.x < -100:
                self.x = 500
                self.y =10000
                self.go_left = True
                p1_ammo_reservs += 1
    def collision(self):
        global P2_STRUCK_DOWN, P2_HP
        if P2_STRUCK_DOWN and P2_Iframes < 185:
            self.y = 1000000
            self.rect.midbottom = self.x , self.y
            screen.blit(self.surf , (self.x , self.y))
            P2_HP -= 1
            P2_STRUCK_DOWN = False
    def reset(self):
        self.y=10000000
class BulletP2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = water_drop_image
        self.rect = self.surf.get_rect()
        self.go_right = False
        self.go_left = False
    def spawn(self,player2):
        global plooking_at_p2
        self.x = player2.pos.x
        self.y = player2.pos.y - 50
        self.rect.midbottom = self.x, self.y
        if plooking_at_p2 == "Left":
            self.go_left = True
            self.go_right = False
        if plooking_at_p2 == "Right":
            self.go_left = False
            self.go_right = True
    def moving(self):
        global p2_ammo_reservs
        self.surf = water_drop_image
        if self.go_right == True:
            self.x += 5
            self.rect.midbottom = self.x , self.y
            screen.blit(self.surf , (self.x , self.y))
            if self.x > Width:
                self.x =500
                self.y = 10000000
                self.go_left = False
                p2_ammo_reservs += 1
        elif self.go_left == True:
            self.x -= 5
            self.rect.midbottom = self.x , self.y
            screen.blit(self.surf, (self.x , self.y))
            if self.x < -100:
                self.x = 500
                self.y =10000
                self.go_left = True
                p2_ammo_reservs += 1
    def collision(self):
        global P1_STRUCK_DOWN, P1_HP
        if P1_STRUCK_DOWN and P1_Iframes < 185:
            self.y = 1000000
            self.rect.midbottom = self.x , self.y
            screen.blit(self.surf , (self.x , self.y))
            P1_HP -= 1
            P1_STRUCK_DOWN = False
    def reset(self):
        self.y=10000000
class platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, hight):
        super().__init__()
        platform_image = pygame.image.load(
            "Platform.png").convert_alpha()
        platform_image = pygame.transform.scale(platform_image , (width , hight))
        self.surf = platform_image
        self.rect = self.surf.get_rect()
        self.plat_y = y

        self.rect = self.surf.get_rect(center=(x, y))
    def return_y(self):
        return self.plat_y

player1 = Player1()
player2 = Player2()
Bullet1 = BulletP1()
Bullet2 = BulletP2()

Bullet_from_player_1 = pygame.sprite.Group()
Bullet_from_player_1.add(Bullet1)
Bullet_from_player_2 = pygame.sprite.Group()
Bullet_from_player_2.add(Bullet2)

Floor = platform(x = Width/2,y = Hight -10,width=Width,hight=20)
jump_platform = platform(x=500, y=500, width=300, hight=20)
jump_platformLU = platform(x=100, y=300, width=300, hight=20)
jump_platformL= platform(x=100, y=600, width=200, hight=20)
jump_platformRU = platform(x=900, y=300, width=300, hight=20)
jump_platformR = platform(x=900, y=600, width=250, hight=20)
platforms = pygame.sprite.Group()
platforms.add(Floor , jump_platform , jump_platformLU , jump_platformR , jump_platformL , jump_platformRU)

all_sprites = pygame.sprite.Group()
all_sprites.add(Floor,player1,jump_platform,jump_platformLU,jump_platformR,jump_platformL,jump_platformRU,player2)

p1_ammo_reservs = 1
p2_ammo_reservs = 1


while not done:
    global no_colls_p1
    pressed_keys = pygame.key.get_pressed()
    screen.fill((10, 119, 122))

    #I frames
    if P1_Iframes > 0: P1_Iframes -= 1
    if P2_Iframes > 0: P2_Iframes -= 1

    #Frames for players
    if frames != 200:
        frames += 1
    elif frames == 200:
        frames = 1
    if plooking_at_p1 == "Right":
        if frames <= 200 and frames >= 150:
            player_image1 = p1_idle_animation[3]
            if P1_Iframes > 0:
                player_image1 =p1_hurt_animation[3]
        if frames <=150 and frames >= 100:
            player_image1 = p1_idle_animation[2]
            if P1_Iframes > 0:
                player_image1 =p1_hurt_animation[2]
        if frames <=100 and frames >= 50:
            player_image1 = p1_idle_animation[1]
            if P1_Iframes > 0:
                player_image1 =p1_hurt_animation[1]
        if frames <=50 and frames >= 0:
            player_image1 = p1_idle_animation[0]
            if P1_Iframes > 0:
                player_image1 =p1_hurt_animation[0]
    if plooking_at_p1 == "Left":
        if frames <= 200 and frames >= 150:
            player_image1 = p1_idle_animation_mirorred[3]
            if P1_Iframes > 0:
                player_image1 =p1_hurt_animation_mirrored[3]
        if frames <=150 and frames >= 100:
            player_image1 = p1_idle_animation_mirorred[2]
            if P1_Iframes > 0:
                player_image1 =p1_hurt_animation_mirrored[2]
        if frames <=100 and frames >= 50:
            player_image1 = p1_idle_animation_mirorred[1]
            if P1_Iframes > 0:
                player_image1 =p1_hurt_animation_mirrored[1]
        if frames <=50 and frames >= 0:
            player_image1 = p1_idle_animation_mirorred[0]
            if P1_Iframes > 0:
                player_image1 =p1_hurt_animation_mirrored[0]

    if plooking_at_p2 == "Right":
        if frames <= 200 and frames >= 150:
            player_image2 = player2_animation[3]
            if P2_Iframes > 0:
                player_image2 =p2_hurt_animation[3]
        if frames <=150 and frames >= 100:
            player_image2 = player2_animation[2]
            if P2_Iframes > 0:
                player_image2 =p2_hurt_animation[2]
        if frames <=100 and frames >= 50:
            player_image2 = player2_animation[1]
            if P2_Iframes > 0:
                player_image2 =p2_hurt_animation[1]
        if frames <=50 and frames >= 0:
            player_image2 = player2_animation[0]
            if P2_Iframes > 0:
                player_image2 =p2_hurt_animation[0]
    if plooking_at_p2 == "Left":
        if frames <= 200 and frames >= 150:
            player_image2 = player2_animation_mirrored[3]
            if P2_Iframes > 0:
                player_image2 =p2_hurt_animation_mirrored[3]
        if frames <=150 and frames >= 100:
            player_image2 = player2_animation_mirrored[2]
            if P2_Iframes > 0:
                player_image2 =p2_hurt_animation_mirrored[2]
        if frames <=100 and frames >= 50:
            player_image2 = player2_animation_mirrored[1]
            if P2_Iframes > 0:
                player_image2 =p2_hurt_animation_mirrored[1]
        if frames <=50 and frames >= 0:
            player_image2 = player2_animation_mirrored[0]
            if P2_Iframes > 0:
                player_image2 =p2_hurt_animation_mirrored[0]

    #Frames for Bullets

    if looked_at_bullet == "Left":
        if frames <= 200 and frames >= 150:
            water_drop_image = water_drop_movement_mirrored[3]
        if frames <=150 and frames >= 100:
            water_drop_image = water_drop_movement_mirrored[2]
        if frames <=100 and frames >= 50:
            water_drop_image = water_drop_movement_mirrored[1]
        if frames <=50 and frames >= 0:
            water_drop_image = water_drop_movement_mirrored[0]
    if looked_at_bullet == "Right":
        if frames <= 200 and frames >= 150:
            water_drop_image = water_drop_movement[3]
        if frames <=150 and frames >= 100:
            water_drop_image = water_drop_movement[2]
        if frames <=100 and frames >= 50:
            water_drop_image = water_drop_movement[1]
        if frames <=50 and frames >= 0:
            water_drop_image = water_drop_movement[0]

    #HP Bars

    #player 1

    if P1_HP == 3:
        hp_bar_p1 = player1_HP_Bar_3.get_rect(center=(62 , 33))
        screen.blit(player1_HP_Bar_3 , hp_bar_p1)
    elif P1_HP == 2:
        hp_bar_p1 = player1_HP_Bar_2.get_rect(center=(62 , 33))
        screen.blit(player1_HP_Bar_2 , hp_bar_p1)
    elif P1_HP == 1:
        hp_bar_p1 = player1_HP_Bar_1.get_rect(center=(62 , 33))
        screen.blit(player1_HP_Bar_1 , hp_bar_p1)
    else:
        hp_bar_p1 = player1_HP_Bar_0.get_rect(center=(62 , 33))
        screen.blit(player1_HP_Bar_0 , hp_bar_p1)

    #player 2
    if P2_HP == 3:
        hp_bar_p2 = player2_HP_Bar_3.get_rect(center=(940 , 33))
        screen.blit(player2_HP_Bar_3 , hp_bar_p2)
    elif P2_HP == 2:
        hp_bar_p2 = player2_HP_Bar_2.get_rect(center=(940 , 33))
        screen.blit(player2_HP_Bar_2 , hp_bar_p2)
    elif P2_HP == 1:
        hp_bar_p2 = player2_HP_Bar_1.get_rect(center=(940 , 33))
        screen.blit(player2_HP_Bar_1 , hp_bar_p2)
    else:
        hp_bar_p2 = player2_HP_Bar_0.get_rect(center=(940 , 33))
        screen.blit(player2_HP_Bar_0 , hp_bar_p2)

    #Reseting
    if P1_HP == 0:
        lost_player_textbox = lost_player_1.get_rect()
        lost_player_textbox.center = (500 , 300)
        screen.blit(lost_player_1 , lost_player_textbox )
        screen.blit(lost_info,lost_info_textbox)
        Bullet1.reset()
        Bullet2.reset()
    elif P2_HP ==0:
        Bullet1.reset()
        Bullet2.reset()
        lost_player_textbox = lost_player_2.get_rect()
        lost_player_textbox.center = (500 , 300)
        screen.blit(lost_player_2 , lost_player_textbox )
        screen.blit(lost_info , lost_info_textbox)
    if pressed_keys[pygame.K_r]:
        has_hit_ground_p1 = True
        has_hit_ground_p2 = True
        frames = 0
        P1_HP = 3
        P2_HP = 3
        player1.respawn()
        player2.respawn()


    #Bullets
    if P1_HP != 0 and P2_HP != 0 :
        Bullet2.moving()
        Bullet2.collision()
        Bullet1.moving()
        Bullet1.collision()


    #Pplayer 1 stuffz
    if pressed_keys[pygame.K_s] and player1.pos.y < 750:
        player1.under_platform()
    else:
        no_colls_p1 = True
    if P1_HP != 0 and P2_HP != 0 :
        player1.movement()
        player1.collisions()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and p1_ammo_reservs != 0 and P1_HP != 0 and P2_HP != 0:
            pos = pygame.mouse.get_pos()
            Bullet1.spawn(player1)
            p1_ammo_reservs = 0
            looked_at_bullet = plooking_at_p1
    if pressed_keys[pygame.K_SPACE] and has_hit_ground_p1 and P1_HP != 0 and P2_HP != 0:
        player1.jumping()
        has_hit_ground_p1  = False



    #player 2 stuff
    if pressed_keys[pygame.K_DOWN] and player2.pos.y < 750:
        player2.under_platform()
    else:
        no_colls_p2 = True
    if P2_HP != 0 and P1_HP != 0 :
        player2.movement()
        player2.collisions()
        if pressed_keys[pygame.K_UP] and has_hit_ground_p2:
            player2.jumping()
            has_hit_ground_p2  = False
        if  pressed_keys[pygame.K_RCTRL] and p2_ammo_reservs != 0:
            Bullet2.spawn(player2)
            p2_ammo_reservs = 0
            looked_at_bullet = plooking_at_p1


    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(120)
pygame.display.flip()