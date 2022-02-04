import pymysql

class GSW:
    def __init__(self,name,ppg,apg,rpg,bid=0):
        self.bid=bid
        self.name=name
        self.ppg=ppg
        self.apg=apg
        self.rpg=rpg
    def __str__(self):
        return "GSW: ID:{} Name:{} PPG:{} APG:{} RPG:{}".format(self.bid,self.name,self.ppg,self.apg,self.rpg)

def addPlayer(GSW):
    connection=pymysql.connect(host='localhost',user='root',password='',db='NBA')
    cursor=connection.cursor()
    query='insert into Dubs(id,name,ppg,apg,rpg)values(%s,%s,%s,%s,%s)'
    cursor.execute(query,(GSW.bid,GSW.name,GSW.ppg,GSW.apg,GSW.rpg))
    connection.commit()
    cursor.close()
    connection.close()
    print('Done')

def getAllPlayers():
    connection=pymysql.connect(host='localhost',user='root',password='',db='NBA')
    cursor=connection.cursor()
    query='select * from Dubs'
    cursor.execute(query)
    data=cursor.fetchall()
    cursor.close()
    connection.close()
    print('Done')
    return data

def getPlayerById(bid):
    connection=pymysql.connect(host='localhost',user='root',password='',db='NBA')
    cursor=connection.cursor()
    query='select * from Dubs where id=%s'
    cursor.execute(query,(bid))
    data=cursor.fetchone()
    cursor.close()
    connection.close()
    return data

def deletePlayerById(bid):
    connection=pymysql.connect(host='localhost',user='root',password='',db='NBA')
    cursor=connection.cursor()
    query='delete from Dubs where id=%s'
    cursor.execute(query,(bid))
    connection.commit()
    cursor.close()
    connection.close()

def updatePlayerById(Dubs):
    connection=pymysql.connect(host='localhost',user='root',password='',db='NBA')
    cursor=connection.cursor()
    query='update Dubs set name=%s, ppg=%s, apg=%s, rpg=%s where id=%s'
    cursor.execute(query,(Dubs.name,Dubs.ppg,Dubs.apg,Dubs.rpg,Dubs.bid))
    connection.commit()
    cursor.close()
    connection.close()
    
##print('ppg=Points per game')
##print('apg=Assist per game')
##print('rpg=Rebound per game')
##p1=GSW('A.Iguodala',7.8,3.0,3.3,9)
##addPlayer(p1)
##p2=GSW("S.Livingston",5.9,3.3,2.2,34)
##addPlayer(p2)
##del_id=int(input('enter the player id to delete'))
##deletePlayerById(del_id)
##update_id=int(input('Enter the id to be updated'))
##old_player=getPlayerById(update_id)
##print(old_player)
##new_name=input('Enter the name to be updated')
##new_ppg=float(input('Enter the ppg to be updated'))
##new_apg=float(input('Enter the apg to be updated'))
##new_rpg=float(input('Enter the rpg to be updated'))
##new_player=GSW(new_name,new_ppg,new_apg,new_rpg,update_id)
##updatePlayerById(new_player)
##players=getAllPlayers()
##print(players)
