from itertools import product

import math

import random

import pygame


clock = pygame.time.Clock()


def start_screen():
    global timer
    n = 0 - DISPLAY_SIZE[0]
    v = 200
    backgraund_image = pygame.image.load('data/start_game_zastavka.png')
    backgraund_image = pygame.transform.scale(backgraund_image, DISPLAY_SIZE)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                timer = 0
                return
        if n < 0:
            n += v * clock.tick() / 1000
        else:
            n = 0
        screen.fill('black')
        screen.blit(backgraund_image, (n, 0))
        pygame.display.flip()


TILE_SIZE = 50


class Tile(pygame.sprite.Sprite):

    type2image = {'.': pygame.transform.scale(pygame.image.load('data/pesok.png'), (TILE_SIZE, TILE_SIZE)),
                  '#': pygame.transform.scale(pygame.image.load('data/skala.png'), (TILE_SIZE, TILE_SIZE)),
                  '1': pygame.transform.scale(pygame.image.load('data/Doroga_1.png'), (TILE_SIZE, TILE_SIZE)),
                  '2': pygame.transform.scale(pygame.image.load('data/Doroga_2.png'), (TILE_SIZE, TILE_SIZE)),
                  '3': pygame.transform.scale(pygame.image.load('data/Doroga_3.png'), (TILE_SIZE, TILE_SIZE)),
                  '4': pygame.transform.scale(pygame.image.load('data/Doroga_4.png'), (TILE_SIZE, TILE_SIZE)),
                  '5': pygame.transform.scale(pygame.image.load('data/Doroga_5.png'), (TILE_SIZE, TILE_SIZE)),
                  '6': pygame.transform.scale(pygame.image.load('data/Doroga_6.png'), (TILE_SIZE, TILE_SIZE)),
                  '7': pygame.transform.scale(pygame.image.load('data/stanzea.png'), (TILE_SIZE, TILE_SIZE)),
                  'D': pygame.transform.scale(pygame.image.load('data/Dom.png'), (TILE_SIZE, TILE_SIZE)),
                  'r': pygame.transform.scale(pygame.image.load('data/rrr.png'), (TILE_SIZE * 2, TILE_SIZE)),
                  'm': pygame.transform.scale(pygame.image.load('data/turel_1_2.png'), (TILE_SIZE, TILE_SIZE)),
                  'c': pygame.transform.scale(pygame.image.load('data/turel_2_2.png'), (TILE_SIZE, TILE_SIZE)),
                  'mm': pygame.transform.rotate(pygame.transform.scale(pygame.image.load('data/motozekl_1.png'), (TILE_SIZE, TILE_SIZE)), 90),
                  'cc': pygame.transform.rotate(pygame.transform.scale(pygame.image.load('data/car.png'), (TILE_SIZE, TILE_SIZE)), 90)

                  }

    def __init__(self, pos, type, *groups):
        super().__init__(*groups)
        if type == 'c' or type == 'm' or type == 'cc' or type == 'mm':
            image = Tile.type2image[type]
            image.set_colorkey(image.get_at((0, 0)))
            self.image = image
        else:
            self.image = Tile.type2image[type]
        self.rect = self.image.get_rect().move(pos)
        self.type = type


class Tile_VOLN(pygame.sprite.Sprite):

    type2image = {
                  'mm': pygame.transform.rotate(pygame.transform.scale(pygame.image.load('data/motozekl_1.png'), (TILE_SIZE, TILE_SIZE)), 90),
                  'cc': pygame.transform.rotate(pygame.transform.scale(pygame.image.load('data/car.png'), (TILE_SIZE, TILE_SIZE)), 90)
                  }

    def __init__(self, pos, type, rote=0, *groups):
        super().__init__(*groups)
        image = pygame.transform.rotate(Tile_VOLN.type2image[type], rote)
        image.set_colorkey(image.get_at((0, 0)))
        self.image = image
        self.rect = self.image.get_rect().move(pos)
        self.type = type


class Tile_Gan(pygame.sprite.Sprite):

    type2image = {
                  't1_1': pygame.transform.rotate(pygame.transform.scale(pygame.image.load('data/turel_1_1.png'), (TILE_SIZE, TILE_SIZE)), 0),
                  't1_2': pygame.transform.rotate(pygame.transform.scale(pygame.image.load('data/turel_1_2.png'), (TILE_SIZE, TILE_SIZE)), 0)
                  }

    def __init__(self, pos, type, rote=0, *groups):
        super().__init__(*groups)
        image = pygame.transform.rotate(Tile_Gan.type2image[type], rote)
        image.set_colorkey(image.get_at((0, 0)))
        self.image = image
        self.rect = self.image.get_rect().move(pos)
        self.type = type


class Tile_PULE(pygame.sprite.Sprite):

    type2image = {
                  'p1': pygame.transform.rotate(pygame.transform.scale(pygame.image.load('data/pula_1.png'), (TILE_SIZE // 3, TILE_SIZE // 3)), 0)
                  }

    def __init__(self, pos, type, rote=0, *groups):
        super().__init__(*groups)
        image = pygame.transform.rotate(Tile_PULE.type2image[type], rote)
        image.set_colorkey(image.get_at((0, 0)))
        self.image = image
        self.rect = self.image.get_rect().move(pos)
        self.type = type


class Tile_time(pygame.sprite.Sprite):

    imagee = {'0': pygame.transform.scale(pygame.image.load('data/0.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '1': pygame.transform.scale(pygame.image.load('data/1.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '2': pygame.transform.scale(pygame.image.load('data/2.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '3': pygame.transform.scale(pygame.image.load('data/3.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '4': pygame.transform.scale(pygame.image.load('data/4.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '5': pygame.transform.scale(pygame.image.load('data/5.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '6': pygame.transform.scale(pygame.image.load('data/6.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '7': pygame.transform.scale(pygame.image.load('data/7.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '8': pygame.transform.scale(pygame.image.load('data/8.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '9': pygame.transform.scale(pygame.image.load('data/9.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  ':': pygame.transform.scale(pygame.image.load('data/tohe.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '=>': pygame.transform.scale(pygame.image.load('data/Nexte.png'), (TILE_SIZE, TILE_SIZE)),
                  'm': pygame.transform.scale(pygame.image.load('data/motozekl_1.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  'c': pygame.transform.scale(pygame.image.load('data/car.png'), (TILE_SIZE // 2, TILE_SIZE))
              }

    def __init__(self, pos, type, *groups):
        super().__init__(*groups)
        self.image = Tile_time.imagee[type]
        self.rect = self.image.get_rect().move(pos)
        self.type = type


class Tile_MINE(pygame.sprite.Sprite):

    imagee = {'0': pygame.transform.scale(pygame.image.load('data/0.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '1': pygame.transform.scale(pygame.image.load('data/1.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '2': pygame.transform.scale(pygame.image.load('data/2.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '3': pygame.transform.scale(pygame.image.load('data/3.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '4': pygame.transform.scale(pygame.image.load('data/4.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '5': pygame.transform.scale(pygame.image.load('data/5.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '6': pygame.transform.scale(pygame.image.load('data/6.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '7': pygame.transform.scale(pygame.image.load('data/7.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '8': pygame.transform.scale(pygame.image.load('data/8.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  '9': pygame.transform.scale(pygame.image.load('data/9.png'), (TILE_SIZE // 2, TILE_SIZE)),
                  'c': pygame.transform.scale(pygame.image.load('data/coin.png'), (TILE_SIZE, TILE_SIZE))
              }

    def __init__(self, pos, type, *groups):
        super().__init__(*groups)
        self.image = Tile_MINE.imagee[type]
        self.rect = self.image.get_rect().move(pos)
        self.type = type


def load_map(path):
    with open(path, mode='r') as in_file:
        return [list(row.rstrip('\n')) for row in in_file]


def generate_level(map):
    tile_group = pygame.sprite.Group()
    playar_group = pygame.sprite.Group()
    playar = None
    for i, j in product(range(len(map)), range(len(map[0]))):
        Tile((j * TILE_SIZE, i * TILE_SIZE), map[i][j], tile_group)
    return playar, tile_group, playar_group


def generate_timer(timer, cord):
    timer_group = pygame.sprite.Group()
    minute = timer // 60
    secund = timer % 60
    Tile_time((650, 0), str(int(minute // 10)), timer_group)
    Tile_time((675, 0), str(int(minute % 10)), timer_group)
    Tile_time((700, 0), ':', timer_group)
    Tile_time((725, 0), str(int(secund // 10)), timer_group)
    Tile_time((750, 0), str(int(secund % 10)), timer_group)
    return timer_group


def generate_mani(mani, mani_group):
    mani_group = pygame.sprite.Group()
    Tile_MINE((650, 100), str(int(mani // 100)), mani_group)
    Tile_MINE((675, 100), str(int((mani % 100) // 10)), mani_group)
    Tile_MINE((700, 100), str(int(mani % 10)), mani_group)
    Tile_MINE((725, 100), 'c', mani_group)
    return mani_group


def generate_VOLN_timer_and_VOLN_score(timer, cord):
    timer_VOLN_group = pygame.sprite.Group()
    minute = timer // 60
    secund = timer % 60
    #Tile_time((650, 50), str(int(minute % 10)), timer_VOLN_group)
    #Tile_time((675, 50), ':', timer_VOLN_group)
    #Tile_time((700, 50), str(int(secund // 10)), timer_VOLN_group)
    #Tile_time((725, 50), str(int(secund % 10)), timer_VOLN_group)
    Tile_time((750, 50), '=>', timer_VOLN_group)
    return timer_VOLN_group


def generate_VOLN_group(colechestvo, tip, time_start, time, hp_povorot_poss, VOLN_group, cords):
    if hp_povorot_poss == 0 and VOLN_group == 0:
        ii = 0
        jj = 0
        curs = load_map('data/aaa2')
        for i, j in product(range(len(curs)), range(len(curs[0]))):
            if curs[i][j] == '1':
                ii = i
                jj = j
        VOLN_group = pygame.sprite.Group()
        hp_povorot_poss = []
        for i in range(colechestvo):
            Tile_VOLN(((0 - TILE_SIZE) * i, ii * TILE_SIZE), tip, 0, VOLN_group)
            hp_povorot_poss.append([100, 0, [int((0 - TILE_SIZE) * i), int(ii * TILE_SIZE)], cords])
        return VOLN_group, hp_povorot_poss
    else:
        for i in VOLN_group:
            i.kill()
        VOLN_group = pygame.sprite.Group()
        for i in range(len(hp_povorot_poss)):
            Tile_VOLN((int(hp_povorot_poss[i][2][0]), int(hp_povorot_poss[i][2][1])), tip, hp_povorot_poss[i][1], VOLN_group)
        return VOLN_group


def generate_Gan_group(colechestvo, tip, GAN_group, gan_povorot_poss):
    if gan_povorot_poss == 0:
        perezoradka = 10
        GAN_group = pygame.sprite.Group()
        gan_povorot_poss = []
        for i in range(colechestvo):
            Tile_Gan(((0 + TILE_SIZE) * i, ii * TILE_SIZE), tip + '_2', 0, GAN_group)
            gan_povorot_poss.append([90, [(0 + TILE_SIZE) * i, ii * TILE_SIZE], tip + '_2', perezoradka])
        return GAN_group, gan_povorot_poss
    else:
        for i in GAN_group:
            i.kill()
        Gan_group = pygame.sprite.Group()
        for i in range(colechestvo):
            Tile_Gan((gan_povorot_poss[i][1][0], gan_povorot_poss[i][1][1]), gan_povorot_poss[i][2], gan_povorot_poss[i][0], GAN_group)
        return GAN_group


def generate_PULE_group(pula_povorot_vector_poss, PULE_group):
    if pula_povorot_vector_poss == 0:
        PULE_group = pygame.sprite.Group()
        pula_povorot_vector_poss = []
        return PULE_group, pula_povorot_vector_poss
    else:
        for i in PULE_group:
            i.kill()
        PULE_group = pygame.sprite.Group()
        for i in range(len(pula_povorot_vector_poss)):
            Tile_PULE(pula_povorot_vector_poss[i][2], 'p1', pula_povorot_vector_poss[i][0], PULE_group)
        return PULE_group


def bashne_cords(name_cart):
    bashne = []
    curs = load_map(name_cart)
    for i, j in product(range(len(curs)), range(len(curs[0]))):
        if curs[i][j] == '7':
            bashne.append([j * TILE_SIZE, i * TILE_SIZE])
    return bashne


def cord_povorot():
    cords = []
    cord_map = load_map('data/aaa2')
    cord_mapp = []
    for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
        cord_mapp.append(cord_map[i][j])
    if '1' in cord_mapp:
        for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
            if cord_map[i][j] == '1':
                cords.append([j, i])
        if '2' in cord_mapp:
            for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
                if cord_map[i][j] == '2':
                    cords.append([j, i])
            if '3' in cord_mapp:
                for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
                    if cord_map[i][j] == '3':
                        cords.append([j, i])
                if '4' in cord_mapp:
                    for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
                        if cord_map[i][j] == '4':
                            cords.append([j, i])
                    if '5' in cord_mapp:
                        for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
                            if cord_map[i][j] == '5':
                                cords.append([j, i])
                        if '6' in cord_mapp:
                            for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
                                if cord_map[i][j] == '6':
                                    cords.append([j, i])
                            if '7' in cord_mapp:
                                for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
                                    if cord_map[i][j] == '7':
                                        cords.append([j, i])
                                if '8' in cord_mapp:
                                    for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
                                        if cord_map[i][j] == '8':
                                            cords.append([j, i])
                                    if '9' in cord_mapp:
                                        for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
                                            if cord_map[i][j] == '9':
                                                cords.append([j, i])
    for i, j in product(range(len(cord_map)), range(len(cord_map[0]))):
        if cord_map[i][j] == 'A':
            cords.append([j, i])
    for i in range(len(cords)):
        cords[i][0] = cords[i][0] * TILE_SIZE
        cords[i][1] = cords[i][1] * TILE_SIZE
    return cords



bashne = bashne_cords('data/aaa.txt')

cords = cord_povorot()

DISPLAY_SIZE = (800, 800)

pygame.init()

screen = pygame.display.set_mode(DISPLAY_SIZE)

start_screen()

timer = 0

timer_start_voln = 0

playar, test_level, playar_group = generate_level(load_map('data/aaa.txt'))

timer_group = generate_timer(timer, 0)

timer_VOLN_group = generate_VOLN_timer_and_VOLN_score(60, 0)

VOLN_group, hp_povorot_poss = generate_VOLN_group(0, 'cc', timer_start_voln, timer, 0, 0, cords)

GAN_group, gan_povorot_poss = generate_Gan_group(0, 't2', 0, 0)

PULE_grop, pula_povorot_vector_poss = generate_PULE_group(0, 0)

timer_VOLN = 0

skipp = 0

voln_skrt = 0

ok_ok = 0

spid_car = 60

gan_dvij = 0

vr_cord = [-50, -50]

cord_on_sprite = [0, 0]

mouse_pos = [0, 0]

mani = 5

timer_last = 0

mani_group = generate_mani(mani, 0)

GAN = pygame.sprite.Group()

dall = []

GAME_OVER = False

min_rast = [1000, 1000]

running = True

while running:
    timer_last = timer
    timer += clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if int(event.button) == 1 and 750 < event.pos[0] < 800 and 50 < event.pos[1] < 100:
                sec = 0
                voln_skrt += 1
                skipp += ((60 - (timer % 60)) - (skipp % 60)) - 1
                curs = load_map('data/aaa2')
                for i, j in product(range(len(curs)), range(len(curs[0]))):
                    if curs[i][j] == '1':
                        ii = i
                for v in range((voln_skrt // 2) + 1):
                    cords = cord_povorot()
                    hp_povorot_poss.append([100, 0, [int((0 - TILE_SIZE) * v), int(ii * TILE_SIZE)], cords])
            elif int(event.button) == 1 and 50 < event.pos[0] < 100 and 550 < event.pos[1] < 600:
                gan_dvij = 1
                cord_on_sprite = [event.pos[0] - 50, event.pos[1] - 550]
        if event.type == pygame.MOUSEBUTTONUP:
            if gan_dvij == 1:
                for i in bashne:
                    if i[0] < (mouse_pos[0] - cord_on_sprite[0]) < i[0] + 50 and i[1] < (mouse_pos[1] - cord_on_sprite[1]) < i[1] + 50:
                        if mani >= 5:
                            gan_povorot_poss.append([90, [i[0], i[1]], 't1_2', 10])
                            mani -= 5
            gan_dvij = 0
            vr_cord = [-50, -50]

    for i in GAN:
        i.kill()

    if gan_dvij == 1:
        Tile((mouse_pos[0] - cord_on_sprite[0], mouse_pos[1] - cord_on_sprite[1]), 'm', GAN)

    for i in range(len(gan_povorot_poss)):
        if gan_povorot_poss[i][1] in bashne:
            pass
        else:
            dall.append(i)

    for i in dall:
        gan_povorot_poss.remove(gan_povorot_poss[i])
    dall = []

    for ii in range(len(gan_povorot_poss)):
        for i in range(len(hp_povorot_poss)):
            if min_rast == [1000, 1000]:
                min_rast = hp_povorot_poss[i][2]
            else:
                if ((gan_povorot_poss[ii][1][0] - hp_povorot_poss[i][2][0]) ** 2 + (gan_povorot_poss[ii][1][1] -
                                                                                    hp_povorot_poss[i][2][1]) ** 2) < \
                        ((gan_povorot_poss[ii][1][0] - min_rast[0]) ** 2 + (gan_povorot_poss[ii][1][1] -
                                                                            min_rast[1]) ** 2):
                    min_rast = hp_povorot_poss[i][2]
        gan_povorot_poss[ii][0] = math.degrees(math.atan2((gan_povorot_poss[ii][1][0] - min_rast[0]), (gan_povorot_poss[ii][1][1] - min_rast[1])))
        gan_povorot_poss[ii][3] = gan_povorot_poss[ii][3] - 5 * (timer - timer_last)
        if gan_povorot_poss[ii][3] <= 0 and min_rast != [1000, 1000]:
            pula_povorot_vector_poss.append([gan_povorot_poss[ii][0], [math.sin(math.radians(gan_povorot_poss[ii][0])), math.cos(math.radians(gan_povorot_poss[ii][0]))], [gan_povorot_poss[ii][1][0] + 20, gan_povorot_poss[ii][1][1] + 20]])
            gan_povorot_poss[ii][3] = 10
        min_rast = [1000, 1000]

    for ii in range(len(pula_povorot_vector_poss)):
        pula_povorot_vector_poss[ii][2][0] -= pula_povorot_vector_poss[ii][1][0] * 1000 * (timer - timer_last)
        pula_povorot_vector_poss[ii][2][1] -= pula_povorot_vector_poss[ii][1][1] * 1000 * (timer - timer_last)
        pula_povorot_vector_poss[ii][0] += 200 * clock.tick() / 1000
        if pula_povorot_vector_poss[ii][0] >= 360:
            pula_povorot_vector_poss[ii][0] -= 360
        for i in range(len(hp_povorot_poss)):
            if hp_povorot_poss[i][2][0] <= pula_povorot_vector_poss[ii][2][0] <= hp_povorot_poss[i][2][0] + 50 and hp_povorot_poss[i][2][1] <= pula_povorot_vector_poss[ii][2][1] <= hp_povorot_poss[i][2][1] + 50:
                dall.append(ii)
                hp_povorot_poss[i][0] -= 50

    for i in dall:
        if len(pula_povorot_vector_poss) >= i + 1:
            pula_povorot_vector_poss.remove(pula_povorot_vector_poss[i])
    dall = []


    cords = cord_povorot()

    for ii in range(len(hp_povorot_poss)):
        ok_ok = 0
        if hp_povorot_poss[ii][0] <= 0:
            mani += 1
            dall.append(ii)
        if hp_povorot_poss[ii][3][0] == hp_povorot_poss[ii][2]:
            if len(hp_povorot_poss[ii][3]) == 1:
                dall.append(ii)
                running = False
            else:
                hp_povorot_poss[ii][3].remove(hp_povorot_poss[ii][3][0])
        elif hp_povorot_poss[ii][3][0][0] == hp_povorot_poss[ii][2][0]:
            if hp_povorot_poss[ii][3][0][1] > hp_povorot_poss[ii][2][1]:
                hp_povorot_poss[ii][1] = 90
                if hp_povorot_poss[ii][3][0][1] - 10 < hp_povorot_poss[ii][2][1]:
                    hp_povorot_poss[ii][2][1] = hp_povorot_poss[ii][3][0][1]
                else:
                    hp_povorot_poss[ii][2][1] += spid_car * (timer - timer_last)
            elif hp_povorot_poss[ii][3][0][1] < hp_povorot_poss[ii][2][1]:
                hp_povorot_poss[ii][1] = 270
                if hp_povorot_poss[ii][3][0][1] + 10 > hp_povorot_poss[ii][2][1]:
                    hp_povorot_poss[ii][2][1] = hp_povorot_poss[ii][3][0][1]
                else:
                    hp_povorot_poss[ii][2][1] -= spid_car * (timer - timer_last)
        elif hp_povorot_poss[ii][3][0][1] == hp_povorot_poss[ii][2][1]:
            if hp_povorot_poss[ii][3][0][0] > hp_povorot_poss[ii][2][0]:
                hp_povorot_poss[ii][1] = 180
                if hp_povorot_poss[ii][3][0][0] - 10 < hp_povorot_poss[ii][2][0]:
                    hp_povorot_poss[ii][2][0] = hp_povorot_poss[ii][3][0][0]
                else:
                    hp_povorot_poss[ii][2][0] += spid_car * (timer - timer_last)
            elif hp_povorot_poss[ii][3][0][0] < hp_povorot_poss[ii][2][0]:
                hp_povorot_poss[ii][1] = 0
                if hp_povorot_poss[ii][3][0][0] + 10 > hp_povorot_poss[ii][2][0]:
                    hp_povorot_poss[ii][2][0] = hp_povorot_poss[ii][3][0][0]
                else:
                    hp_povorot_poss[ii][2][0] -= spid_car * (timer - timer_last)

    for i in dall:
        if len(hp_povorot_poss) >= i + 1:
            hp_povorot_poss.remove(hp_povorot_poss[i])
    dall = []

    timer_group = generate_timer(timer, 13 * TILE_SIZE)

    mani_group = generate_mani(mani, mani_group)

    VOLN_group = generate_VOLN_group(len(hp_povorot_poss), 'cc', timer_start_voln, timer, hp_povorot_poss, VOLN_group,
                                     cords)

    timer_VOLN_cope = int(timer_VOLN)

    timer_VOLN = ((60 - (timer % 60)) - (skipp % 60)) % 61

    sec = 0

    if int(timer_VOLN) != timer_VOLN_cope:
        sec += 1

    if sec >= 60:
        sec = 0
        voln_skrt += 1

    timer_VOLN_group = generate_VOLN_timer_and_VOLN_score(timer_VOLN, 0)

    GAN_group = generate_Gan_group(len(gan_povorot_poss), 't1', GAN_group, gan_povorot_poss)

    PULE_group = generate_PULE_group(pula_povorot_vector_poss, PULE_grop)

    screen.fill('black')
    test_level.draw(screen)
    playar_group.draw(screen)
    timer_group.draw(screen)
    timer_VOLN_group.draw(screen)
    mani_group.draw(screen)
    PULE_group.draw(screen)
    VOLN_group.draw(screen)
    GAN_group.draw(screen)
    GAN.draw(screen)
    pygame.display.flip()

pygame.quit()