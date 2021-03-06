from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.utils import simplejson
from sh import ping
from pinger.models import Host, Runstatus, Bot
from datetime import datetime
import socket
import json
import time
import threading

STOP = False
NUMBER_OF_PINGS = 2
DEADLINE = 3
hosts = ['192.168.186.1', '192.168.186.2', '192.168.186.3', '192.168.186.4','192.168.186.5','192.168.186.6', '192.168.186.7']
ICQ_VALID_CODE = '12345678'
ICQ_SERVER_IP = 'localhost'
ICQ_SERVER_PORT = 1235
PATH_TO_BOT_SHELL = '/home/hate2pay/bot/bot.sh'
HOST_GROUP_SIZE = 2


def stop_bot():
	'''Stops bot process shell. If process ID is not 0 or 1 it tries to stop it, writes new PID = 0 to Database
	and returns True. Else returns False.'''
	import os, signal
	pr = Bot.objects.get(id=1)
	if pr.p_id and pr.p_id != 1:
		os.killpg(pr.p_id, signal.SIGTERM)
		pr.p_id = 0
		pr.save()
		return True
	return False
def run_bot():
	'''This function makes ICQ bot run. It uses subprocess to run subprocess python shell. If bot is not already running
	run_bot function starts it and writes PID to the Database. Returns True, if bot process was started, else returns False'''
	import subprocess, os
	pr = Bot.objects.get(id=1)
	if not pr.p_id:
		#path = os.path.dirname(os.path.abspath(__file__)) + pr.path
		p = subprocess.Popen(pr.path, shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
		pr.p_id = p.pid
		pr.save()
		return True

	return False

def stop_or_run_bot(path):
	"""This simple function makes ICQ bot run or stop it. It takes 2 arguments, 
		first - path to bot in your system and second subprocess of running bot! If the subprocess is None, 
		this function makes bot to start run, else it stops the subprocess"""
	import os
	import signal
	import subprocess
	pr = Bot.objects.get(id=1)
	if pr.p_id:
		os.killpg(pr.p_id, signal.SIGTERM)
		pr.p_id = 0
		PR.save()
		return False
	try:
		p = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
		pr.p_id = p.pid
		pr.save()
	except:
		return False
	
	return True



def send_data_loop():

	def send_data(data, s):
		data_dict = {ICQ_VALID_CODE:data}
		data = bytes(json.dumps(data_dict), 'ascii')
		s.send(data)

	def make_chuncks(hosts, n):
		for i in range(0, len(hosts), n):
			yield hosts[i:i+n]

	def ping_proc(hosts, s):
		for host in hosts:
			status = Runstatus.objects.get(id=1)
			if not status.status:
				return None
			try:
				ping('-c', NUMBER_OF_PINGS, '-w', DEADLINE, host.ipaddr)
			except:
				if host.up_status:
					host.up_status = False
					host.host_down_time = datetime.now()
					host.save()
					data = host.name + ' is down! ' + time.strftime("%H:%M:%S")
					send_data(data, s)
			else:
				if not host.up_status:
					host.up_status = True
					host.host_down_time = None
					host.save()
					data = host.name + ' is up!' + time.strftime("%H:%M:%S")
					send_data(data, s)


	while True:
		status = Runstatus.objects.get(id=1)
		if not status.status:
			return None
		time.sleep(5) # Need time to ICQ bot load
		s = socket.socket()
		s.connect((ICQ_SERVER_IP, ICQ_SERVER_PORT))
		hosts = Host.objects.all()
		hosts_groups = list(make_chuncks(hosts, HOST_GROUP_SIZE))
		my_threads = []
		for i in range(0, len(hosts_groups), 1):
			hosts = hosts_groups[i]
			name = 't' + str(i)
			my_threads.append(threading.Thread(target = ping_proc, name = name, args = [hosts, s]).start())

		while not threading.activeCount() == 1:
			time.sleep(1)


def valid_user(user):
	if not user.is_authenticated():
		return False
	if not user.is_staff:
		return False
	return True



def pinger_main_page(request):
	if not request.user.is_authenticated():
		error = "You need to login first!"
		return render_to_response('login.html', { 'err': error, })
	user = request.user
	perm = True if user.is_staff else False
	status = Runstatus.objects.get(id=1)
	run = status.status
	return render_to_response('base.html', { 'user':user, 'perm':perm, 'run':run })

def run_pinger(request):
	if not request.user.is_authenticated():
		error = "You need to login first!"
		return render_to_response('login.html', { 'err': error, })
	if not request.user.is_staff:
		raise Http404
	if not request.is_ajax():
		raise Http404
	if not valid_user(request.user):
		raise Http404
	status = Runstatus.objects.get(id=1)
	user = request.user
	perm = True if user.is_staff else False
	if status.status:
		warning = 'You\'ve just tried to RUN pinger, but it\'s already RUNNING!'
		return render_to_response ('base.html', { 'user':user, 'perm':perm, 'warning':warning })
	pr = Bot.objects.get(id=1)
	pr = run_bot()
	if not pr:
		warning = 'You\'ve just tried to RUN pinger, but something went wrong with ICQ bot when it tried to run ' + str(pr)
		return render_to_response ('base.html', { 'user':user, 'perm':perm, 'warning':warning })
	try:
		status.status = True
		status.save()
	except:
		status.status = False
		status.save()
		stop_bot()
		response_dict = {'server_response':'something went wrong when Runner tried to activate send_data_loop function!'}
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	else:
		send_data_loop()
	response_dict = {'server_response':'Evrything must work!'}
	return HttpResponseRedirect('/pinger')

def stop_pinger(request):
	if not request.is_ajax():
		raise Http404
	if not valid_user(request.user):
		raise Http404
	user = request.user
	perm = True if user.is_staff else False
	status = Runstatus.objects.get(id=1)
	if not status.status:
		stop_bot()
		warning = 'You\'ve just tried to STOP pinger, but it\'s NOT RUNNING at the moment!'
		return render_to_response ('base.html', { 'user':user, 'perm':perm, 'warning':warning, 'run':status})
	try:
		stop_bot()
	except:
		status.status = False
		status.save()
		warning = 'You\'ve just tried to STOP pinger, but something went wrong when programm tried to stop ICQ bot!'
		return render_to_response ('base.html', { 'user':user, 'perm':perm, 'warning':warning, 'run':status })
	else:
		status.status = False
		status.save()
	warning = 'Don\'t worry be happy'
	return HttpResponseRedirect('/pinger')

def update_table(request):
	if not request.is_ajax():
		raise Http404
	switches = Host.objects.filter(up_status = False)
	return render_to_response('table.html', {'switches':switches})