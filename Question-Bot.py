import spacy, wikipedia

nlp = spacy.load('en')

def again(): #again function gives the user the oppurtunity to ask other questions
    try:
        Again = input("Would you like to enter more questions?")

        if Again in 'y Y YES yes Yes'.split():
            main()
        elif Again in 'no n NO N No'.split():
            quit()
    except:
        print("Please enter either yes or no:\n")
        again()

def main():
    while True:
        try:
            Question = input("Please enter a properly puncuated question:\n")
            break
        except:
            (KeyboardInterrupt, ValueError) #allows for exceptions and does not break or close

    doc = nlp(Question)

    sentences = doc.sents
    entities = doc.ents
    ncs = doc.noun_chunks

    question_type = []
    question_details = []


    for word in doc:
        if word.pos_ == 'ADV':                  #if word in 'who where what why how when'.split():  did not work
            question_type.append(word)

        elif word.pos_ == 'NOUN':
            question_type.append(word)
            question_details.append(word)

        elif word.pos_ == 'VERB':
            question_details.append(word)

        elif word.pos_ == 'ADJ':
            question_details.append(word)       #categorises different types of words into question details and question type

    #print("Question type is {0}\n".format(question_type))
    #print("Question details are {0}\n".format(question_details))
    
    for n in ncs:
        target_subject = n
        #print("Target subject is {0}\n".format(target_subject))
    
    #for ent in entities:
        #print("Entites are {0}n\n".format(ent.label_))
        
    a = str(target_subject)

    split_a = a.split()
    url = ""
    
    for word in split_a:                    #word.replace(' ', '_') did not work
        if word != split_a[-1]:
            word = word + "_"
            url = url + word

        else:
            url = url + split_a[-1]

    try:
        Adress = wikipedia.page(url)
    except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError):
            print("Sorry, but there is no Wikipedia article about your question.\n")
            again()
                                         
    Content = Adress.content
    nlp_content = nlp(Content)
    sents = nlp_content.sents

    for sentence in sents:
        for word in sentence:
            if word in question_details and question_type:
                print(sentence)

    again()


main()
