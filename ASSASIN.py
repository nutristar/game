import random
import time
start_time = time.time()
#import me4
#import topor

class Warior:

    h=0
    p=0
    w=0
    def weapon(self, fw):
        self.w = fw             #
    def setH (self,fh):
        self.h=fh

    def setP (self, fp):
        self.p=fp#*fw              #оружие  влияет на силу удара, почему так не работает?


    def udar (self, enemy):                #получение удара
        self.h = self.h - enemy.p*enemy.w

    def getH(self):
        return self.h

asassin = Warior()
asassin.setH(100000)
asassin.setP(1)
asassin.weapon(1)

knight = Warior()
knight.setH(100000)
knight.setP(1)
knight.weapon(1)   # правильно?

#knight.udar(asassin)
print("У АСАСИНА здоровье -", asassin.h, "У АСАСИНА удар -",asassin.p, "\n", "у РЫЦАРЯ здоровье -",knight.h,  "У Рыцаря удар -", knight.p )



while asassin.h > 0 and knight.h > 0:
    x = random.randint(0, 1)
    #print(x)
    if x==0:
        knight.udar(asassin)

    elif x==1:
        asassin.udar(knight)


    #print("ass h =", asassin.h)
    #print("kn h =", knight.h)

if knight.h<=0 :
    print("assasin win", "его здоровье равно-", asassin.h)
else:
    print("knight win", "его здоровье равно-", knight.h)


print("--- %s seconds длился бой ---" % (time.time() - start_time))

