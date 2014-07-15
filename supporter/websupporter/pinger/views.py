from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.utils import simplejson
from sh import ping
from pinger.models import Host, Runstatus
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

def stop_or_run_bot(path, pr):
	"""This simple function makes ICQ bot run or stop it. It takes 2 arguments, 
		first - path to bot in your system and second subprocess of running bot! If the subprocess is None, 
		this function makes bot to start run, else it stops the subprocess"""
	import os
	import signal
	import subprocess
	if pr:
		os.killpg(pr.pid, signal.SIGTERM)
		return False
	try:
		pr = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
	except:
		return False
	
	return pr



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
					data = host.name + ' is down!'
					send_data(data, s)
			else:
				if not host.up_status:
					host.up_status = True
					host.host_down_time = None
					host.save()
					data = host.name + ' is up!'
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
		send_data(str(bot_run_process), s)
		my_threads = []
		for i in range(0, len(hosts_groups), 1):
			hosts = hosts_groups[i]
			name = 't' + str(i)
			my_threads.append(threading.Thread(target = ping_proc, name = name, args = [hosts, s]).start())
			'''for th in my_threads:
				send_data(str(th), s)
				#th.start()'''
		while not threading.activeCount() == 1:
			time.sleep(1)
		'''for host in hosts:
			status = Runstatus.objects.get(id=1)
			if not status.status:
				break
			try:
				ping('-c', NUMBER_OF_PINGS, '-w', DEADLINE, host.ipaddr)
			except:
				if host.up_status:
					host.up_status = False
					host.host_down_time = datetime.now()
					host.save()
					data = host.name + ' is down!'
					send_data(data, s)
			else:
				if not host.up_status:
					host.up_status = True
					host.host_down_time = None
					host.save()
					data = host.name + ' is up!'
					send_data(data, s)
		s.close()'''

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
	'''if not request.user.is_authenticated():
		error = "You need to login first!"
		return render_to_response('login.html', { 'err': error, })
	if not request.user.is_staff:
		raise Http404'''
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
	pr = stop_or_run_bot(PATH_TO_BOT_SHELL, False)
	if not pr:
		warning = 'You\'ve just tried to RUN pinger, but something went wrong with ICQ bot when it tried to run'
		return render_to_response ('base.html', { 'user':user, 'perm':perm, 'warning':warning })
	global bot_run_process
	bot_run_process = pr #write bot process to this value
	try:
		status.status = True
		status.save()
		#send_data_loop()
	#except:
	#send_data_loop()
	except:
		status.status = False
		status.save()
		stop_or_run_bot(PATH_TO_BOT_SHELL, bot_run_process)
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
		warning = 'You\'ve just tried to STOP pinger, but it\'s NOT RUNNING at the moment!'
		return render_to_response ('base.html', { 'user':user, 'perm':perm, 'warning':warning, 'run':status})
	try:
		stop_or_run_bot(PATH_TO_BOT_SHELL, bot_run_process)
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
