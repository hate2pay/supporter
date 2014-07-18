#!/usr/bin/env python


from twisted.words.protocols import oscar
from twisted.internet import protocol, reactor
from twisted.internet.defer import Deferred
import getpass
import json

SN = '693040329' # replace this with a screenname
PASS =  'omgMs69F' # replace this with a password
ICQ_VALID_CODE = '12345678' #need to confirm recieved data
RECIEVERS = ['413420257', '411488951']

if SN[0].isdigit():
    icqMode = 1
    hostport = ('login.icq.com', 5238)
else:
    hostport = ('login.oscar.aol.com', 5190)
    icqMode = 0

class B(oscar.BOSConnection):
    capabilities = [oscar.CAP_CHAT]
    def initDone(self):
        self.requestSelfInfo().addCallback(self.gotSelfInfo)
        self.requestSSI().addCallback(self.gotBuddyList)
    def gotSelfInfo(self, user):
        print user.__dict__
        self.name = user.name
    def gotBuddyList(self, l):
        print l
        self.activateSSI()
        self.setProfile('''Hello, I\'m ICQ helper =)!. I use ICMP to check the availability of switches in the network. If something changes, I tell my friends about it. Contact my developer, if you want to be my friend! (hate2pay@sputnik-nt.dn.ua)''')
        self.setIdleTime(0)
        self.clientReady()
        #self.createChat('%s Chat'%SN).addCallback(self.createdRoom)
    '''def createdRoom(self, (exchange, fullName, instance)):
        print 'created room',exchange, fullName, instance
        self.joinChat(exchange, fullName, instance).addCallback(self.chatJoined)
    def updateBuddy(self, user):
        print user
    def offlineBuddy(self, user):
        print 'offline', user.name'''
    def receiveMessage(self, user, multiparts, flags):
        print user.name, multiparts, flags
	self.sendMessage(user.name, 'Hello, I\'m ICQ helper =)!. I use ICMP to check the availability of switches in the network. If something changes, I tell my friends about it. Contact my developer, if you want to be my friend! (hate2pay@sputnik-nt.dn.ua)')
        self.getAway(user.name).addCallback(self.gotAway, user.name)
        if multiparts[0][0].find('away')!=-1:
            self.setAway('I am away from my computer right now.')
        elif multiparts[0][0].find('back')!=-1:
            self.setAway(None)
        '''if self.awayMessage:
            self.sendMessage(user.name,'<html><font color="#0000ff">'+self.awayMessage,autoResponse=1)
        else:
            self.lastUser = user.name
            self.sendMessage(user.name, multiparts, wantAck = 1, autoResponse = (self.awayMessage!=None)).addCallback( \
                self.messageAck)'''
    def messageAck(self, (username, message)):
        print 'message sent to %s acked' % username
    def gotAway(self, away, user):
        if away != None:
            print 'got away for',user,':',away
    '''def receiveWarning(self, newLevel, user):
        print 'got warning from', hasattr(user,'name') and user.name or None
        print 'new warning level', newLevel
        if not user:
            #username = self.lastUser
            return 
        else:
            username = user.name
        self.warnUser(username).addCallback(self.warnedUser, username)
    def warnedUser(self, oldLevel, newLevel, username):
        self.sendMessage(username,'muahaha :-p')
    def receiveChatInvite(self, user, message, exchange, fullName, instance, shortName, inviteTime):
            print 'chat invite from',user.name,'for room',shortName,'with message:',message
            self.joinChat(exchange, fullName, instance).addCallback(self.chatJoined)
    def chatJoined(self, chat):
        print 'joined chat room', chat.name
        print 'members:',map(lambda x:x.name,chat.members)
    def chatReceiveMessage(self, chat, user, message):
        print 'message to',chat.name,'from',user.name,':',message
        if user.name!=self.name: chat.sendMessage(user.name+': '+message)
        if message.find('leave')!=-1 and chat.name!='%s Chat'%SN: chat.leaveChat()
    def chatMemberJoined(self, chat, member):
        print member.name,'joined',chat.name
    def chatMemberLeft(self, chat, member):
        print member.name,'left',chat.name
        print 'current members',map(lambda x:x.name,chat.members)
        if chat.name!="%s Chat"%SN and len(chat.members)==1:
            print 'leaving', chat.name
            chat.leaveChat()'''

class OA(oscar.OscarAuthenticator):
   BOSClass = B

oscar_prot = None

def get_B_instance(b_instance):
    global oscar_prot
    oscar_prot = b_instance

d = Deferred()
d.addCallback(get_B_instance)


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        try:
            #data = type(data)
            #str(data)
            data = json.loads(data.decode('ascii'))
            data = data[ICQ_VALID_CODE]
            data = json.dumps(data)
            data = data[1:-1]
            #start_index = data.find(ICQ_VALID_CODE)
            #data = start_index
        except:
            return None
            #data = 'Not valid data recieved'

    	#data = data + '\nKHMEL molodec! \n'
    	#self.transport.write(data)
        for rec in RECIEVERS:
    	   oscar_prot.sendMessage(rec, data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(1235, EchoFactory())


protocol.ClientCreator(reactor, OA, SN, PASS, deferred=d, icq=icqMode).connectTCP(*hostport)
reactor.run()
