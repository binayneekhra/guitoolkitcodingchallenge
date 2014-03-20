# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    #session.forget()
    hintLevelForm=SQLFORM.factory(Field('hintName',
                                 label='Please choose the Hint Level',
                                 requires=IS_IN_SET(['No Hint', 'Source Hint (Basque Sentence)', 'Machine Translation Hint (Apertium Sentence)', 'Both Source and Machine Translation Hint'])
                                 ))  
    
    if hintLevelForm.process().accepted:
        #redirect to cloze test
        session.hintName = request.vars.hintName
        redirect(URL('clozeTest'))#, vars =dict(hintName=hintName)))

    return dict(hintLevelForm=hintLevelForm)
    #@author=Binay Neekhra, neekhra.binay@gmail.com
def clozeTest():
    hintName = session.hintName
    
    #START find the right sentence    
    sentences = db().select(db.sentence.ALL)
    testcase = db.sentence(id>0)#for dummy value
    
    if hintName == 'No Hint':
        for testcase in sentences:
            if testcase.flagNoHint == False:
                break
    elif hintName == 'Source Hint (Basque Sentence)':
        for testcase in sentences:
            if testcase.flagSourceHint == False:
               break
    elif hintName == 'Machine Translation Hint (Apertium Sentence)':
        for testcase in sentences:
            if testcase.flagApertiumHint == False:
                break
    elif hintName == 'Both Source and Machine Translation Hint':
       for testcase in sentences:
            if testcase.flagBothHints == False:
                break
    #END find the right sentence    
    
    maskedWords = []
    temp=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen']
    wordPairDict = {}
    words = testcase.reference.split()
    for i in range(len(words)):
            if ((i+1)%5==0):
                maskedWords.append(words[i])
                modifiedWord= words[i]+'tail' #for avoiding special keywords 'for' 'is' 'in'
                wordPairDict[modifiedWord] = 'temp'

    session.testcase = testcase
    session.words = words
    session.maskedWords = maskedWords
    session.wordPairDict=wordPairDict
    session.temp = temp
        
    d='t'
    #after submit button pressed    
#    if request.vars.cloze:
#        response.flash = 'pass'
#        d = 'ohh'
 #       session.d = d
 #       redirect(URL('thankyou'))#, vars =dict(hintName=hintName, testcase=testcase, words=words, maskedWords=maskedWords, wordPairDict=wordPairDict)))
#        hello='hello'
        #iterate over all
#    for i in range(len(words)/5):
          #  db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.wordPairDict[maskedWords[0]])
       # db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord='maksed', userGuess=request.vars.single)
   # else:
   #     response.flash = 'blocked'
   #     d = 'ohh'
  #      redirect(URL('index'))    
    return dict(hintName=hintName, testcase=testcase, words=words, maskedWords=maskedWords, wordPairDict=wordPairDict, temp=temp)

def thankyou():    
#        clozeTable0 = db().select(db.clozeWords.ALL, orderby=db.clozeWords.sentenceID)
    #d = redirect(URL('clozeTest'))
    #testcase = redirect(URL('clozeTest'))
    ##words = redirect(URL('clozeTest')) 
    #maskedWords = redirect(URL('clozeTest')) 
    #wordPairDict = redirect(URL('clozeTest'))  
    hintName = session.hintName
   # d = session.d 
    testcase = session.testcase
    words = session.words
    maskedWords = session.maskedWords
    wordPairDict=session.wordPairDict
    temp = session.temp

    #response.flash = d
    
    if hintName == 'No Hint':  
        db(db.sentence.id==testcase.id).update(flagNoHint=True) 
    elif hintName == 'Source Hint (Basque Sentence)':
        db(db.sentence.id==testcase.id).update(flagSourceHint =True)
    elif hintName == 'Machine Translation Hint (Apertium Sentence)':
        db(db.sentence.id==testcase.id).update(flagApertiumHint   =True) 
    elif hintName == 'Both Source and Machine Translation Hint':  
        db(db.sentence.id==testcase.id).update(flagBothHints=True)    
    
    for i in range(len(words)/5):

        if i==0:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.zero) #wordPairDict[maskedWords[i]+'tail'])
        
        elif i==1:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.one) #wordPairDict[maskedWords[i]+'tail'])
            
        elif i==2:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.two) #wordPairDict[maskedWords[i]+'tail'])
        
        elif i==3:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.three) #wordPairDict[maskedWords[i]+'tail'])
        elif i==4:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.four) #wordPairDict[maskedWords[i]+'tail'])
        
        elif i==5:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.five) #wordPairDict[maskedWords[i]+'tail'])
            
        elif i==6:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.six) #wordPairDict[maskedWords[i]+'tail'])
        
        elif i==7:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.seven) #wordPairDict[maskedWords[i]+'tail'])
            
          #<complete this>  
        elif i==8:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.eight) #wordPairDict[maskedWords[i]+'tail'])
        
        elif i==9:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.nine) #wordPairDict[maskedWords[i]+'tail'])
            
        elif i==10:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.ten) #wordPairDict[maskedWords[i]+'tail'])
        
        elif i==11:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.eleven) #wordPairDict[maskedWords[i]+'tail'])
        elif i==12:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.twelve) #wordPairDict[maskedWords[i]+'tail'])
        
        elif i==13:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.thirteen) #wordPairDict[maskedWords[i]+'tail'])
            
        elif i==14:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.fourteen) #wordPairDict[maskedWords[i]+'tail'])
        
        elif i==15:
            db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[i], userGuess=request.vars.fifteen) #wordPairDict[maskedWords[i]+'tail'])
    
    
    
    
    
    #dictKey = maskedWords[0]+'tail'
        #request.vars.   
       # form = eval(wordPairDict[dictKey]) 
    #db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord=maskedWords[0], userGuess=request.vars.wordPairDict[dictKey]) #wordPairDict[maskedWords[i]+'tail'])

    #db.clozeWords.insert(sentenceID=testcase.id, hintLevel=hintName, referenceWord='maksed', userGuess=request.vars.single)
           
    return dict(hintName=hintName, testcase=testcase, words=words, maskedWords=maskedWords, wordPairDict=wordPairDict)

#@auth.requires_membership('admin')
def viewRecords():
    #myquery = (db.mytable.myfield != None) | (db.mytable.myfield > 'A')
    notEvaluated = db( (db.sentence.flagNoHint == False) &
                       (db.sentence.flagSourceHint == False) &
                       (db.sentence.flagApertiumHint == False) &
                       (db.sentence.flagBothHints == False)).select(db.sentence.ALL)

    evaluated = db( (db.sentence.flagNoHint == True) |
                       (db.sentence.flagSourceHint == True) |
                       (db.sentence.flagApertiumHint     == True) |
                       (db.sentence.flagBothHints == True)).select(db.sentence.ALL)

    return dict(notEvaluated=notEvaluated, evaluated=evaluated)

#@auth.requires_membership('admin')
def results():
    
    evaluatedNoHint = db(db.sentence.flagNoHint == True).select(db.sentence.ALL)
    evaluatedSourceHint = db(db.sentence.flagSourceHint == True).select(db.sentence.ALL)
    evaluatedApertiumHint = db(db.sentence.flagApertiumHint == True).select(db.sentence.ALL)    
    evaluatedBothHints = db(db.sentence.flagBothHints    == True).select(db.sentence.ALL)


    clozeTable0 = db(db.clozeWords.hintLevel == 'No Hint').select(db.clozeWords.ALL)
    clozeTable1 = db(db.clozeWords.hintLevel == 'Source Hint (Basque Sentence)').select(db.clozeWords.ALL)
    clozeTable2 = db(db.clozeWords.hintLevel == 'Machine Translation Hint (Apertium Sentence)').select(db.clozeWords.ALL)
    clozeTable3 = db(db.clozeWords.hintLevel == 'Both Source and Machine Translation Hint').select(db.clozeWords.ALL)

    #wordPairDict={} #contains word pair, with their sentence id

    #for pair in clozeTable0:
    #    wordpairs=[]
    #    correctResponse=0
    #    blanksLeft=0
    #    for sentence in evaluatedNoHint:
    #        singlePair=[]
    #        if pair.sentenceID  == sentence.id:
    #            singlePair.append( pair.referenceWord)
    #            singlePair.append( pair.userGuess)
    #            if pair.referenceWord==pair.userGuess:
    #                correctResponse +=1
    #            elif pair.userGuess=='':
    #                blanksLeft +=1
    #
    #        wordpairs.append(singlePair)
    #    wordpairs.append(correctResponse)
    #    wordpairs.append(blanksLeft)
    #    wordPairDict[sentence.id] = wordpairs

    correctResponse=0
    blanksLeft=0
    totalResponse=0

    return dict(evaluatedNoHint=evaluatedNoHint,  clozeTable0=clozeTable0, clozeTable1=clozeTable1,clozeTable2=clozeTable2, clozeTable3=clozeTable3, correctResponse=correctResponse, blanksLeft=blanksLeft, totalResponse=totalResponse, evaluatedSourceHint=evaluatedSourceHint, evaluatedApertiumHint=evaluatedApertiumHint, evaluatedBothHints=evaluatedBothHints ) # ,wordPairDict=wordPairDict


#@auth.requires_membership('admin')
def addSentences():
    form = SQLFORM(db.sentence)
    if form.process().accepted:
        response.flash = 'record inserted'
    else:
        response.flash = 'please fill the form'
    return dict(form=form)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
