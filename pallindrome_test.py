#looks for 4 bit pallindromes
import pop_v1
import random
import winsound
reload(pop_v1)
def make_qs(n):
    qs=[]
    ans=[]
    for i in range(n):
        a=random.choice([0,1])
        b=random.choice([0,1])
        c=random.choice([0,1])
        d=random.choice([0,1])
        if a==d and b==c:
            ans+=[1]
        else:
            ans+=[0]
        qs+=[[a,b,c,d]]
    return qs, ans

def step(pop, its=1, alert=False):
    #Calls some functions on the pop. The net will be modified. No real need to return it, so it doesn't
    #Second argument is number of steps to go through. Prints output after every step, only makes an alert after the last step
    #If you pass "True" as the third argument, it will play whatever sound on your (Windows) computer is set to "Question". See control panel/sounds
    try:
        for i in range(its):
            qs,ans=make_qs(1000)
            pop.test(qs,ans)
            print pop.fancy_stats()
            pop.cull()
            pop.repop()
        if alert:
            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
    except:
        if alert:
            try:
                #Play a bad alert sound
                winsound.Playsound("SystemHand", winsound.SND_ALIAS)
            except:
                print "Winsound is broken. Set the 'alert' argument to False."
                raise
            raise
    
def make_pop(n):
    return pop_v1.population(4,2,n,[4,4,4])