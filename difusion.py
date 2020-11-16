from ipAddress import ipAddressMask

def difusionIp(ip):
	temp_ip = ip.split('.')
	mask = ipAddressMask(ip).split('.')
	res = []
	for x in range(4):
		if mask[x] == '255':
			res.append(temp_ip[x])
		else:res.append('0')
	return ".".join(res)
