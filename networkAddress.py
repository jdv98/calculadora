from ipAddress import ipAddressMask

def networkAddress(ip):
	temp_ip = ip.split('.')
	mask = ipAddressMask(ip).split('.')
	res1 = []
	for x in range(4):
		if mask[x] == '255':
			res1.append("11111111")
	res2 = []
	for x in range(4):
		if mask[x] == '0':
			res2.append("00000000")
	return {"network":".".join(res2),"host":".".join(res1)}