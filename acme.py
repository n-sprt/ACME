from SimpleCV import *
from sklearn.cluster import KMeans
from sklearn import metrics
import cv2
import pygame
import numpy as np
from pygame.locals import *
import pickle

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)



class ObjectLists:
    pickled = []
    sounds = []
    images = []
    @staticmethod
    def reset_sounds():
        if len(ObjectLists.sounds) > 0:
            del ObjectLists.sounds[:]
    
class Players:    
    @staticmethod
    def one_note_player():
        ObjectLists.sounds[0].play_sound()
    @staticmethod
    def two_note_player():
        ObjectLists.sounds[0].play_sound()
        ObjectLists.sounds[1].play_sound()
    @staticmethod
    def three_note_player():
        ObjectLists.sounds[0].play_sound()
        ObjectLists.sounds[1].play_sound()
        ObjectLists.sounds[2].play_sound()
    @staticmethod
    def four_note_player():
        ObjectLists.sounds[0].play_sound()
        ObjectLists.sounds[1].play_sound()
        ObjectLists.sounds[2].play_sound()
        ObjectLists.sounds[3].play_sound()
    @staticmethod
    def five_note_player():
        ObjectLists.sounds[0].play_sound()
        ObjectLists.sounds[1].play_sound()
        ObjectLists.sounds[2].play_sound()
        ObjectLists.sounds[3].play_sound()
        ObjectLists.sounds[4].play_sound()
    @staticmethod
    def six_note_player():
        ObjectLists.sounds[0].play_sound()
        ObjectLists.sounds[1].play_sound()
        ObjectLists.sounds[2].play_sound()
        ObjectLists.sounds[3].play_sound()
        ObjectLists.sounds[4].play_sound()
        ObjectLists.sounds[5].play_sound()

class Scale:
    screening = False
    newtoncount = 0
    zvcount = 0
    
    @staticmethod
    def get_score(meal):
        del Scale.newtoncount[0]
        del Scale.zvcount[0]
        print("Scoring image for Scales...")
        Scale.screen(meal)
        
    @staticmethod
    def routen(note):
        if Scale.screening is False:
            SOperations.create_soundobj(note)
        if Scale.screening is True:
            Scale.newtoncount += 1
    
    @staticmethod
    def routezv(note):
        if Scale.screening is False:
            SOperations.create_soundobj(note)
        if Scale.screening is True:
            Scale.zvcount += 1
    
            
    @staticmethod      
    def run_newton(meal):
        for i in meal:
            colortup = i
            print(colortup)
            Scale.newton(colortup)
            
    @staticmethod       
    def run_zv(meal):
        for i in meal:
            colortup = i
            print(colortup)
            Scale.zv(colortup)
            
    @staticmethod       
    def screen(meal):
        Scale.screening = True
        for i in Routing.scales:
            for j in meal:
                i(j)
        else:
            Scale.screening = False
            
    
    @staticmethod
    def newton(colortup):

        """ C:   R: 247 G: 13 B: 4

            D:   R: 250 G: 126 B: 14

            E:   R: 245 G: 243 B: 62

            F:   R: 19 G: 142 B: 55

            G:   R: 24 G: 17 B: 127

            A:   R: 129 G: 6 B: 128

            B:   R: 217 G: 19 B: 134
        """
        if 255 > colortup[0] > 200:
            if 50 > colortup[1] > 10 and 10 > colortup[2] > 0:
                Scale.routen('c')
            elif 160 > colortup[1] > 90 and 30 > colortup[2] > 10:
                Scale.routen('d')
            elif 255 > colortup[1] > 200 and 30 > colortup[2] > 10:
                Scale.routen('e')
            elif 40 > colortup[1] > 10 and 160 > colortup[2] > 90:
                Scale.routen('b')
        elif 140 > colortup[0] > 90:
            if 10 > colortup[1] > 0 and 140 > colortup[2] > 90:
                Scale.routen('a')
        elif 60 > colortup[0] > 0:
            if 30 > colortup[1] > 10 and 160 > colortup[2] > 90:
                Scale.routen('g')
            elif 180 > colortup[1] > 120 and 80 > colortup[2] > 20:
                Scale.routen('f')
        elif 10 > colortup[0] > 0:                 # watch out for white
            if 10 > colortup[1] > 0 and 10 > colortup[2] > 0:
                pass
        elif 255 > colortup[1] > 200 and 255 > colortup[2] > 200:     # watch out for black
                pass
        
        if Scale.screening is False:
            if len(ObjectLists.sounds) == 0:
                print "No notes added"
            else:
                print(len(ObjectLists.sounds), "added.")
        
    @staticmethod
    def zv(colortup):
        """ C:     R:188 G: 226 B: 45
            C#:    R: 23 G: 141 B: 55
            D:     R: 27 G: 143 B: 134
            D#:    R: 32 G: 12 B: 133
            E:     R: 130 G: 6 B: 126
            F:     R: 221 G: 16 B: 133
            F#:    R: 114 G: 13 B: 67
            G:     R: 174 G: 5 B: 7
            G#:    R: 246 G: 13 B: 14
            A:     R: 244 G: 128 B: 23
            A#:    R: 234 G: 240 B: 141
            B:     R: 239 G: 246 B: 64
        """
        
        if 255 > colortup[0] > 200:
            if 0 > colortup[1] > 10 and 160 > colortup[2] > 90:
                Scale.routezv('f')
                print("f added")
            elif 60 > colortup[1] > 10 and 60 > colortup[1] > 10:
                Scale.routezv('g#')
                print("g# added")
            elif 160 > colortup[1] > 90 and 60 > colortup[2] > 10:
                Scale.routezv('a')
                print("a added")
            elif 255 > colortup[1] > 200 and 200 > colortup[2] > 140:
                Scale.routezv('a#')
                print("a# added")
            elif 255 > colortup[1] > 130 and 140 > colortup[2] > 90:
                Scale.routezv('d')
                print('d added')
            elif 150 > colortup[1] > 140 and 70 > colortup[2] > 30:
                Scale.routezv('c#')
                print('c# added')
        elif 10 > colortup[0] > 0:        # watch out for white
            if 10 > colortup[1] > 0 and 10 > colortup[2] > 0:
                pass
        if Scale.screening is False: 
            print(colortup)
            if len(ObjectLists.sounds) == 0:
                print("No notes added")        

    
class Routing:
    scales = [Scale.zv, Scale.newton]
    @staticmethod
    def scale_router(meal, scale=None):
        
        if scale == None:
            print(len(meal), "Clusters")
            print('Pick a scale')
            print('newton ({})').format(Scale.newtoncount)
            print('zieverink (zv) ({})').format(Scale.zvcount)
            print('auto')
            print('')
            print('cancel')
            scale = raw_input('>>')

        if scale == 'newton':
            Scale.run_newton(meal)     
        elif scale == 'zieverink' or scale == 'zv':
            Scale.run_zv(meal)
        elif scale == 'auto':
            # Scale.screening = True
            # Scale.screen(meal) ----> taken care of by get_score
            if Scale.newtoncount > Scale.zvcount:
                print("Playing Newton's scale")
                Scale.run_newton(meal)
            elif Scale.zvcount > Scale.newtoncount:
                print("Playing Zieverink's scale")
                Scale.run_zv(meal)
            else:
                print("No scale to play the clustered colors")
        elif scale == 'cancel':
            main()
        else:
            print("Please enter a scale")
            Routing.scale_router(meal)
                    
            
    
    @staticmethod
    def serve(meal):
        Routing.scale_router(meal)
        
            
class SOperations:  
    @staticmethod
    def play():
        if len(ObjectLists.sounds) > 0:
            print("Enter y to play sound")
            go = raw_input("")

            if go == "y":
                if len(ObjectLists.sounds) == 1:
                    Players.one_note_player()
                elif len(ObjectLists.sounds) == 2:
                    Players.two_note_player()
                elif len(ObjectLists.sounds) == 3:
                    Players.three_note_player()
                elif len(ObjectLists.sounds) == 4:
                    Players.four_note_player()
                elif len(ObjectLists.sounds) == 5:
                    Players.five_note_player()
                elif len(ObjectLists.sounds) == 6:
                    Players.six_note_player()
                elif len(ObjectLists.sounds) == 0:
                    print("Error: no sounds to play.")
            else:
                print("Image yielded no chords")

    @staticmethod
    def create_soundobj(note):
        sobj = SObject(note)
        sobj.set_sound()
        ObjectLists.sounds.append(sobj)
        
class IOperations():
    
    @staticmethod  
    def prepare(img):
        """
        http://www.alanzucconi.com/2015/05/24/how-to-find-the-main-colours-in-an-image/
        kmeans preparation. 
        
        recipe:
        
        + convert BGR colorspace to RGB
        + resize the image (smaller field, for speed)
        + flatten the image (1D array of points)
        
        """
        try:
            image = cv2.imread(img,1)
        except:
            "unknown error"
        try:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        except:
            print('Looks like your filepath is empty.')
            print('Check your path and try again.')
        h, w, c = image.shape
        w_new = int(100 * w / max(w, h))
        h_new = int(100 * h / max(w, h))
        
        image = cv2.resize(image, (w_new, h_new))
        image_array = image.reshape((image.shape[0] * image.shape[1], 3))
        
        clt = KMeans(n_clusters = IOperations.centrifuge(image_array))
        clt.fit(image_array)
        
        hist = IOperations.centroid_histogram(clt)
        # sorts the clusters according to how many pixels
        # are present
        zipped = zip(hist, clt.cluster_centers_)
        zipped.sort(reverse=True, key=lambda x : x[0])
        hist, clt.cluster_centers_ = zip(*zipped)
        return clt.cluster_centers_


    @staticmethod
    def centrifuge(image_array): # finds the best clusters
        bestSilhouette = -1
        bestClusters = 0
        count = 0
        
        print('*Finding best clusters....... (silhouette method by Adrian Rosebrock)')
        print('http://www.alanzucconi.com/2015/05/24/how-to-find-the-main-colours-in-an-image/')
        for clusters in range(2, 10):

            clttemp = KMeans(n_clusters = clusters)
            clttemp.fit(image_array)

            silhouette = metrics.silhouette_score(image_array, clttemp.labels_, metric ='euclidean')

            if silhouette > bestSilhouette:
                bestSilhouette = silhouette
                bestClusters = clusters;
            print("/ * \ Spin ", count + 1, "of 8")
            count+=1

        return bestClusters
    
    @staticmethod
    def centroid_histogram(clt):
        # here we're creating a histogram based on the number
        # of pixels assigned to each cluster. 

        #we grab the number of different clusters and create a 
        #histogram based on the number of pixels assigned to each 
        #cluster

        numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
        (hist, _) = np.histogram(clt.labels_, bins = numLabels)

        hist = hist.astype('float')
        hist /= hist.sum()

        return hist

    
class IObject:
    def __init__(self):
        self.image = None
        self.meal = None
        self.name = None
        
    def get_image(self):
        try:
            ansy = raw_input('Enter a complete filepath: ') 
            if ansy == "1":
                access_library()
            elif "/" in ansy:
                print('Loading image')
                return ansy
        except:
            print("Unknown error")

class SObject():
    def __init__(self, note):
        self.note = note
        self.sound = None
    
    def set_sound(self):
        "try:" 
        if self.note == 'c':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/c.wav')
            print('c added')
        elif self.note == 'c#':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/c#.wav')
            print('c# added')
        elif self.note == 'd':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/d.wav')
            print('d added')
        elif self.note == 'd#':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/d#.wav')
            print('d# added')
        elif self.note == 'e':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/e.wav')
            print('e added')
        elif self.note == 'f':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/f.wav')
            print('f added')
        elif self.note == 'f#':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/f#.wav')
            print('f# added')
        elif self.note == 'g':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/g.wav')
            print('g added')
        elif self.note == 'g#':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/g#.wav')
            print('g# added')
        elif self.note == 'a':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/a.wav')
            print('a added')
        elif self.note == 'a#':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/a#.wav')
            print('a# added')
        elif self.note == 'b':
            self.sound = pygame.mixer.Sound('/Users/lachrimare/Documents/Sorry/sounds/b.wav')
            print('b added')
        """except:
            print("Unable to load sound.")"""
            
    def play_sound(self):
        if self.sound != None:
            pygame.mixer.Sound.play(self.sound)
            
def about():
    print('')

                
def access_library():
    print("Enter a number to load an image")
    print("Or enter 'q' to exit")
    for i in range(len(ObjectLists.images)):
        print(ObjectLists.images[i].name, "(", i, ")")
    
    answer = int(raw_input('>> '))
    
    if answer == 'q':
        main()
    else:
        load_library_image(answer)
                    
def load_library_image(answer):
    print(answer)
    for k in range(len(ObjectLists.images)):
        print(k, answer)
        if k == answer:
            print("Load image ", ObjectLists.images[k].name, "?")
            answer = raw_input('>> (y/n)')
            answer.lower()
            if answer != "y" and answer != "n":
                print("Please enter 'y' for yes or 'n' for no.")
                answer = raw_input('>>')
            if answer == 'y':
                print("Image Loaded")
                if ObjectLists.images[k].meal is not None:
                    eggs_and_ham(ObjectLists.images[k])
                    clean_up()
                elif ObjectLists.images[k].meal is None:
                    prepare_and_serve(ObjectLists.images[k])
                    clean_up(ObjectLists.images[k])
                    

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
        
def exit_survey(img, mode='n'):
    if mode == 'c':
        print('Add to library? ')
        print('>>(y/n) ')
        print("Creative mode On. Enter 'n' to turn off.")
    if mode == 'n':
        print("To analyze the last image with another scale press 1 ")
        print("To add the last image to your library press 2 ")
        print("To analyze a new image press 3 ")
        print("To view the image library press 4 ")
        print("To read more about Color and Music press 5")
        print('To save a .txt of your data press 6')
        print("""**To turn on creative mode enter '7'. This turns off the exit survey
              and allows you to continuously load new images (you can still add to library.""")
        ans = raw_input('>> ')
        
        
        if ans == "1":
            eggs_and_ham(img)
        elif ans == "2":
            print("Image name")
            img.name = raw_input(">> ")
            ObjectLists.images.append(img)
        elif ans == "3":
            main()
        elif ans == "4":
            access_library()
        elif ans == "5":
            print('// \\ Under Construction \\ //')
        elif ans == '6':
            file_open()
            file_write()

        else:
            print("Enter 1, 2, 3, 4, 5 or 'c'")
            
snake = IObject()
ObjectLists.images.append(snake)
rainbow = IObject()
ObjectLists.images.append(rainbow)
snake.image = '/Users/lachrimare/Documents/Sorry/colorfulsnake.jpg'
snake.name = 'Colorful Snake'
rainbow.image = '/Users/lachrimare/Documents/Sorry/rainbow-02.png'
rainbow.name = 'Rainbow'

        
def eggs_and_ham(img):
    Routing.serve(img.meal)
    SOperations.play()
    clean_up(img)

def makeisob(img):
    if img.image is None:
        try:
            img.image = img.get_image()
            print("Good choice")
        except TypeError:
            print('''Oops! Seems it's not an image. Check your file.''')
    print("Commencing cluster analysis")
    meal = IOperations.prepare(img.image)
    img.meal = meal
    Scale.get_score(meal)
    Routing.serve(img.meal)
    
def cheese_block():
    img = IObject()
    return img
    
def prepare_and_serve(img):
    makeisob(img)
    SOperations.play()
    
def clean_up(img):
    ObjectLists.reset_sounds()
    exit_survey(img)
    
def main():
    img = cheese_block()
    prepare_and_serve(img)
    clean_up(img)
    
def first_time_round():
    print('Project Obton')
    print('Arcane Color-Music Explorer (ACME) v 1.01')
    print('--')
    print('Test the analogies between sound and light.')
    
while True:
    first_time_round()
    main()
    
    
