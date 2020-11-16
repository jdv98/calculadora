from ipAddress import ipAddressMask

def networkHost(ip):
	temp_ip = ip.split('.')
	mask = ipAddressMask(ip).split('.')
	res1 = []
	for x in range(4):
		if mask[x] == '255':
			res1.append(temp_ip[x])
	res2 = []
	for x in range(4):
		if mask[x] == '0':
			res2.append(temp_ip[x])
	return {"network":".".join(res2),"host":".".join(res1)}