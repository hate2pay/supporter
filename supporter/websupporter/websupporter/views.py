from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from sup.supforweb5 import portactivate, sysinfo, showlog, showprofile, looptest, iptest, errortest, mactest, cablediag
from django.utils import simplejson
from supporter.models import Ipaddress


def start(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/main')
	return render_to_response('login.html')


def login(request):
	if request.method == 'POST':
		try:
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			user = auth.authenticate(username=username, password=password)
		except:
			return render_to_response('login.html')
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/main')
		else:
			error = "Wrong password or username!"
			return render_to_response('login.html', { 'err': error, })
	return render_to_response('login.html')

def authenticate_user(request):
	if not request.user.is_authenticated():
		error = "You need to login first!"
		return render_to_response('login.html', { 'err': error, })
	if 'REMOTE_ADDR' in request.META:
		client_address = request.META['REMOTE_ADDR']
	try:
		user = User.objects.get(username=request.user.username)
		uipob = user.ipaddress_set.get(allowed_ip=client_address)
	except Ipaddress.DoesNotExist:
		error = "You're not allowed to login from this ip address!"
		return render_to_response('login.html', { 'err': error, })

def main(request):

	MAX_PORT_NUMBER = 29
	MAX_SWITCH_NUMBER = 254
	#ALLOWED_IP_ADDRESS = ['192.168.186.2', '192.168.186.3', '192.168.186.4', '192.168.186.5', '192.168.186.7', '192.168.186.8']
	NETWORKS = ['10.248.0.0/24', '10.248.8.0/24', '10.248.24.0/24', '10.248.32.0/24', '10.248.40.0/24', '10.250.0.0/24', '10.250.1.0/24']
	ports = []
	switches = []
	if not request.user.is_authenticated():
		error = "You need to login first!"
		return render_to_response('login.html', { 'err': error, })
	if 'REMOTE_ADDR' in request.META:
		client_address = request.META['REMOTE_ADDR']
	try:
		user = User.objects.get(username=request.user.username)
		uipob = user.ipaddress_set.get(allowed_ip=client_address)
	except Ipaddress.DoesNotExist:
		error = "You're not allowed to login from this ip address!"
		return render_to_response('login.html', { 'err': error, })
	#if not client_address in ALLOWED_IP_ADDRESS:
	#	error = "You're not allowed to login from this ip address!"
	#	return render_to_response('login.html', { 'err': error, })
	for i in range(1, MAX_PORT_NUMBER, 1):
		ports.append(str(i))
	for i in range(1, MAX_SWITCH_NUMBER, 1):
		switches.append(str(i))
	#u = User.objects.get(username=request.user.username)
	#us = str(u.ipaddress_set.get(allowed_ip=client_address))
	objects = request.POST.items()
	network_ch = request.POST.get('net', '')
	switch_ch = request.POST.get('switch', '')
	port_ch = request.POST.get('port', '')
	userip = request.POST.get('userip', '')
	vendor = request.POST.get('vendor', '')
	flag = request.POST.get('showoutput', '')
	allinfo = request.POST.get('allinfo', '')
	button = request.POST.get('btn', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = "Hello, "+ request.user.username + "! Please, choose your test! "
	if button == "Cable Diagnostic":
		massage = cablediag(target_swith, port_ch, allinfo, vendor)
	elif button == "Show MAC on Switchport":
		massage = mactest(target_swith, port_ch, allinfo, vendor)
	elif button == "Link Diagnostics":
		massage = errortest(target_swith, port_ch, allinfo, vendor)
	elif button == "IP DHCP Snooping":
		massage = iptest(target_swith, port_ch, allinfo, vendor, userip)
	elif button == "Switchport Status":
		massage = looptest(target_swith, port_ch, allinfo, vendor)
	elif button == "Activate Switchport":
		massage = portactivate(target_swith, port_ch, allinfo, vendor)
	elif button == "View Switch Info":
		massage = sysinfo(target_swith, port_ch, allinfo, vendor)
	elif button == "Show Switch Log":
		massage = showlog(target_swith, port_ch, allinfo, vendor)
	elif button == "View Multicast Groups":
		massage = showprofile(target_swith, port_ch, allinfo, vendor)
	return render_to_response('index_ajax1.html', { 'user':request.user.username, 'objects':objects, \
		'userip':userip, 'vendor':vendor, 'flag':flag, 'allinfo':allinfo, 'ports':ports, \
		'switches':switches, 'networks':NETWORKS, 'network_ch':network_ch, 'port_ch':port_ch, 'switch_ch':switch_ch, 'massage':massage, })

def logout(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	auth.logout(request)
	return render_to_response('logout.html')

"""def ajax_query(request):
	network_ch = request.GET.get('network_ch', '')
	switch_ch = request.GET.get('switch_ch', '')
	port_ch = request.GET.get('port_ch', '')
	userip = request.GET.get('userip', '')
	vendor = request.GET.get('vendor', '')
	allinfo = request.GET.get('allinfo', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = errortest(target_swith, port_ch, allinfo, vendor)                 
	response_dict = {}                                         
	response_dict.update({'server_response': massage })                                                                  
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

def ajax_mac(request):
	network_ch = request.GET.get('network_ch', '')
	switch_ch = request.GET.get('switch_ch', '')
	port_ch = request.GET.get('port_ch', '')
	userip = request.GET.get('userip', '')
	vendor = request.GET.get('vendor', '')
	allinfo = request.GET.get('allinfo', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = mactest(target_swith, port_ch, allinfo, vendor)                
	response_dict = {}                                         
	response_dict.update({'server_response': massage })                                                                  
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	
def ajax_cable(request):
	network_ch = request.GET.get('network_ch', '')
	switch_ch = request.GET.get('switch_ch', '')
	port_ch = request.GET.get('port_ch', '')
	userip = request.GET.get('userip', '')
	vendor = request.GET.get('vendor', '')
	allinfo = request.GET.get('allinfo', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = cablediag(target_swith, port_ch, allinfo, vendor)               
	response_dict = {}                                         
	response_dict.update({'server_response': massage })                                                                  
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

def ajax_ip(request):
	network_ch = request.GET.get('network_ch', '')
	switch_ch = request.GET.get('switch_ch', '')
	port_ch = request.GET.get('port_ch', '')
	userip = request.GET.get('userip', '')
	vendor = request.GET.get('vendor', '')
	allinfo = request.GET.get('allinfo', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = iptest(target_swith, port_ch, allinfo, vendor, userip)                 
	response_dict = {}                                         
	response_dict.update({'server_response': massage })                                                                  
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

def ajax_portstatus(request):
	network_ch = request.GET.get('network_ch', '')
	switch_ch = request.GET.get('switch_ch', '')
	port_ch = request.GET.get('port_ch', '')
	userip = request.GET.get('userip', '')
	vendor = request.GET.get('vendor', '')
	allinfo = request.GET.get('allinfo', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = looptest(target_swith, port_ch, allinfo, vendor)                
	response_dict = {}                                         
	response_dict.update({'server_response': massage })                                                                  
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

def ajax_port(request):
	network_ch = request.GET.get('network_ch', '')
	switch_ch = request.GET.get('switch_ch', '')
	port_ch = request.GET.get('port_ch', '')
	userip = request.GET.get('userip', '')
	vendor = request.GET.get('vendor', '')
	allinfo = request.GET.get('allinfo', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = portactivate(target_swith, port_ch, allinfo, vendor)               
	response_dict = {}                                         
	response_dict.update({'server_response': massage })                                                                  
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

def ajax_info(request):
	network_ch = request.GET.get('network_ch', '')
	switch_ch = request.GET.get('switch_ch', '')
	port_ch = request.GET.get('port_ch', '')
	userip = request.GET.get('userip', '')
	vendor = request.GET.get('vendor', '')
	allinfo = request.GET.get('allinfo', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = ""
	massage = massage + str(sysinfo(target_swith, port_ch, allinfo, vendor))                
	response_dict = {}                                         
	response_dict.update({'server_response': massage })                                                                  
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

def ajax_log(request):
	network_ch = request.GET.get('network_ch', '')
	switch_ch = request.GET.get('switch_ch', '')
	port_ch = request.GET.get('port_ch', '')
	userip = request.GET.get('userip', '')
	vendor = request.GET.get('vendor', '')
	allinfo = request.GET.get('allinfo', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = ""
	massage = massage + str(showlog(target_swith, port_ch, allinfo, vendor))                
	response_dict = {}                                         
	response_dict.update({'server_response': massage })                                                                  
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

def ajax_multicast(request):
	network_ch = request.GET.get('network_ch', '')
	switch_ch = request.GET.get('switch_ch', '')
	port_ch = request.GET.get('port_ch', '')
	userip = request.GET.get('userip', '')
	vendor = request.GET.get('vendor', '')
	allinfo = request.GET.get('allinfo', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = ""
	massage = massage + str(showprofile(target_swith, port_ch, allinfo, vendor))                
	response_dict = {}                                         
	response_dict.update({'server_response': massage })                                                                  
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')"""

def ajax_tools(request):
	test_id = request.GET.get('test_id', '')
	network_ch = request.GET.get('network_ch', '')
	switch_ch = request.GET.get('switch_ch', '')
	port_ch = request.GET.get('port_ch', '')
	userip = request.GET.get('userip', '')
	vendor = request.GET.get('vendor', '')
	allinfo = request.GET.get('allinfo', '')
	target = network_ch.split("0/")
	target_swith = target[0] + switch_ch
	massage = ""
	if test_id == '1':
		test_result = str(errortest(target_swith, port_ch, allinfo, vendor))
	elif test_id == '2':
		test_result = str(cablediag(target_swith, port_ch, allinfo, vendor))
	elif test_id == '3':
		test_result = str(mactest(target_swith, port_ch, allinfo, vendor))
	elif test_id == '4':
		test_result = str(iptest(target_swith, port_ch, allinfo, vendor, userip))
	elif test_id == '5':
		test_result = str(looptest(target_swith, port_ch, allinfo, vendor))
	elif test_id == '6':
		test_result = str(portactivate(target_swith, port_ch, allinfo, vendor))
	elif test_id == '7':
		test_result = str(sysinfo(target_swith, port_ch, allinfo, vendor))
	elif test_id == '8':
		test_result = str(showlog(target_swith, port_ch, allinfo, vendor))
	elif test_id == '9':
		test_result = str(showprofile(target_swith, port_ch, allinfo, vendor))
	else:
		test_result = "Test ID Error!"
	massage = massage + test_result                
	response_dict = {}                                         
	response_dict.update({'server_response': massage })                                                                  
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')