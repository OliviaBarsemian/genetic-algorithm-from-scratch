import random
# target phrase: human mitochondrial DNA
target = "GATCACAGGTCTATCACCCTATTA"

class Phrase:
    def __init__(self):
        self.characters = []
        #create a random string of the same length
        for i in range(len(target)):
            character = chr(random.choice(range(32, 127)))
            self.characters.append(character)

            #initial fitness will be declared as 0
            self.fitness = 0

    def getContents(self):
        return ''.join(self.characters)
    
    def getFitness(self):
        #count how many characters match the target phrase
        for i in range(len(target)):
            if target[i] == self.characters[i]:
                self.fitness = self.fitness + 1
        return self.fitness

        # save and return fitness
    
    def crossOver(self, partner): 
        #create a new phrase objece by creating a child phrase by mixing characters from self and partner
        child = Phrase()

        for i in range(len(self.characters)):
            if random.random() < 0.5:
                child.characters[i] = self.characters[i]
            else: 
                child.characters[i] = partner.characters[i]
        return child
        
    def mutate(self):
        #for each character, there is a 1% chance it changes to something random
        #help to escape when things get stuck
        for i in range(len(self.characters)):
            if random.random() < 0.01:
                self.characters[i] = chr(random.choice(range(32, 127)))
