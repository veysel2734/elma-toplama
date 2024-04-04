#pgzero

import random

WIDTH = 800
HEIGHT = 600

TITLE = "Bahçe Oyunu"
FPS = 60

elmalar = [Actor("elma.png", (random.randint(50, WIDTH - 50), 0)) for _ in range(5)]

sepet = Actor("sepet.png", (WIDTH // 2, HEIGHT - 50))
ek_resim = Actor("ek_resim.png", (random.randint(50, WIDTH - 50), 0))
skor = 0
oyun_devam_ediyor = True  
bahce_arkaplan = Actor("bahce_arkaplan.png")
bahce_arkaplan.pos = (400, 305)  

def yeni_elma(elma):
    elma.x = random.randint(50, WIDTH - 50)
    elma.y = 0

def yeni_ek_resim(): 
    ek_resim.x = random.randint(50, WIDTH - 50)
    ek_resim.y = 0

def update(dt): 
    global skor, oyun_devam_ediyor
    if not oyun_devam_ediyor:
        return  
    for elma in elmalar:
        elma.y += 5  
        if elma.y > HEIGHT:
            yeni_elma(elma)  
        if sepet.colliderect(elma):
            skor += 1
            yeni_elma(elma) 
    ek_resim.y += 3  
    if ek_resim.y > HEIGHT:
        yeni_ek_resim()  
    if sepet.colliderect(ek_resim):
        skor -= 1  
        yeni_ek_resim() 
        oyun_devam_ediyor = False  
    
def draw():
    
    screen.clear()
    bahce_arkaplan.draw()

    for elma in elmalar:
        elma.draw()  
    sepet.draw()
    ek_resim.draw() 
    screen.draw.text("Skor: " + str(skor), (10, 10), color="white")
    if not oyun_devam_ediyor:
        screen.draw.text("Kaybettin!", center=(WIDTH // 2, HEIGHT // 2), color="red", fontsize=48)

def on_mouse_move(pos):
    sepet.x = pos[0]

for elma in elmalar:
    yeni_elma(elma) 
yeni_ek_resim()  

bahce_arkaplan.image = "bahce_arkaplan"  
