import json







class Question:
    def __init__(self, titre, choix):
        self.titre = titre
        self.choix = choix
        

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
       
        print("QUESTION")
        indice_question = 0
   
        score = 0
        for i in range(len(self.gestion_titre())):
            print(f"Question {i+1} : {self.gestion_titre()[indice_question]}")
            for i in range(len(self.reponse_choix(0, indice_question))):
                print("  ", i+1, "-", self.reponse_choix(0, indice_question)[i])

            print()
            resultat_response_correcte = False
            reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
            if self.reponse_choix(1, indice_question)[reponse_int -1] == True:
                print("Bonne réponse")
                resultat_response_correcte = True
                score += 1


                
            else:
                print("Mauvaise réponse")
                
            print()
            indice_question +=1
        print("Score final :",score ,"sur", (len(self.gestion_titre())))
        
        return resultat_response_correcte
        
    

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
       
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)


    def reponse_choix(self,indice_type, indice_choix):  #indice_type=1 gestion true false // indice_type =0 reponse       
        choix = [ques['choix'] for ques in questionnaire_data['questions']]
        return [reponse[indice_type] for reponse in choix[indice_choix]]
    
    def gestion_titre(self):
        return [ques['titre'] for ques in questionnaire_data['questions']]
    
   
  
    
class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        #print(self.question)
        for question in self.questions:
            if question.poser():
                score += 1
                
        #print("Score final :",score , "sur 10")
        return score


chargemment = True

while chargemment:

    try:
        filename = "arts_museedulouvre_debutant.json"
        file = open(filename, "r")
        json_data = file.read()      
        file.close()
        questionnaire_data = json.loads(json_data)
        chargemment = False
        
    except:
        from import_quizz import open_quizz_db_data


   
Questionnaire(
    (
    Question([ques['titre'] for ques in questionnaire_data['questions']],[reponse[0] for reponse in questionnaire_data['questions'][0]['choix']]), 
    
    )
).lancer()


