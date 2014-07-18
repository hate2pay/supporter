from django.db import models

class Host(models.Model):
	name = models.CharField(max_length=30, verbose_name='Host location')
	ipaddr = models.IPAddressField(verbose_name='Host IP')
	up_status = models.BooleanField(verbose_name = 'Switch status(False = Down, True = Up)')
	host_down_time = models.DateTimeField(verbose_name = 'Time when host has gone to down state', blank = True, null = True)
	description = models.TextField(verbose_name = 'Host Description(not required)', blank = True, null = True)
		

class Runstatus(models.Model):
	status = models.BooleanField(verbose_name = 'EasyPinger run status(False = Down, True = Up)', unique = True)
	name = models.CharField(max_length=30, verbose_name='Status name')
	
class Bot(models.Model):
	path = models.CharField(max_length=60, verbose_name='Path to Bot shell in your system')
	p_id = models.IntegerField(blank = True, verbose_name='Bot Process ID')		
