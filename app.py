from flask import Flask,render_template,request,redirect
from BBall import *

app=Flask(__name__)
#here we are creating object name app,
#which points to the application
@app.route('/',methods=['get'])
def index():
    #return "<h1>Home Page</h1>"
    return render_template('index.html')

@app.route('/login',methods=['post'])
def login():
    return "<h1>Login Page</h1>"


@app.route('/getroster',methods=['get'])
def showroster():
    data=getAllPlayers()
    #data is the tuple of tuples
    return render_template('Roster.html',Roster=data)

@app.route('/addplayer')
def showadd():
    return render_template('addplayer.html',)   

@app.route('/saveplayer',methods=['post'])
def saveplayer():
    Id=request.form['id']
    bid=int(Id)
    name=request.form['name']
    ppg=request.form['ppg']
    apg=request.form['apg']
    rpg=request.form['rpg']
    ppg_num=float(ppg)
    apg_num=float(apg)
    rpg_num=float(rpg)
    player=GSW(name,ppg_num,apg_num,rpg_num,bid)
    addPlayer(player)
    return redirect('/getroster')

@app.route('/deleteplayer/<int:i>')
def deleteplayer(i):
    deletePlayerById(i)
    return redirect('/getroster')

@app.route('/getplayer/<int:i>')
def getplayer(i):
    b=getPlayerById(i)
    return render_template('updateplayer.html',player=b)

@app.route('/updateplayer',methods=['post'])
def updateplayer():
    #fetch all 5 values from update form
    i=request.form['bid']
    bid=int(i)
    name=request.form['name']
    points=request.form['ppg']
    ppg=float(points)
    assist=request.form['apg']
    apg=float(assist)
    rebounds=request.form['rpg']
    rpg=float(rebounds)
    p=GSW(name,ppg,apg,rpg,bid)#create player obj
    updatePlayerById(p)#call BBall update
    return redirect('/getroster')#take the user to /getroster

'''
@app.route('/hello')
def hello():
    return "<h1>Hello from Flask</h1>"


#to run the app,
#write the following code:
'''

if __name__=='__main__':
    app.run(debug=True)

