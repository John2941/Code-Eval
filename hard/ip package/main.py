"""
@Project Name - ip package hard
@author - Johnathan
@date - 2/13/2016
@time - 10:12 AM

https://www.codeeval.com/open_challenges/154/

recalculate the ip checksum after changing the source and destination ip from a packet
"""

import sys

class packet(object):

	def __init__(self, package):
		self.packet = package
		self.iphl = self.parse_IPH()


	def parse_IPH(self):
		"""

		:return: only the ip header
		"""
		ip_header_length = int(self.packet[0][1], 16) * 4  # take the second nibble of the header and multiply by 4
		hexed_packet = []
		for x in self.packet[:ip_header_length]:
			first_nib = hex(int(x[0],16))
			second_nib = hex(int(x[1],16))
			combined = first_nib + second_nib[2:]
			hexed_packet.append(combined)
		return hexed_packet

	def change_IPs(self, sip, dip):
		iphl = self.iphl[:12]
		hex_new_sip = [hex(int(x)) for x in sip.split('.')]
		hex_new_dip = [hex(int(x)) for x in dip.split('.')]
		iphl.extend(hex_new_sip)
		iphl.extend(hex_new_dip)
		new_checksum = self.recalculate_checksum(iphl)  # return hex without 0x; e.g., hex = 47eb not 0x47eb
		first_byte_of_cs = int(new_checksum[:2],16)
		second_byte_of_cs = int(new_checksum[2:],16)
		iphl.insert(10, hex(first_byte_of_cs))
		iphl.insert(11, hex(second_byte_of_cs))
		if self.validate_checksum(iphl):
			code_eval = []
			for x in iphl:
				# print format for code eval challenge
				code_eval.append(x[2:].zfill(2))
			return " ".join(code_eval)

	def recalculate_checksum(self, header):
		del(header[10])  # removes checksum byte 11
		del(header[10])	  # removes check byte 12
		total = 0
		for x in xrange(len(header[::2])):
			# Takes 1 byte and concatenates it to the next byte via bit shifting
			# e.g., 0x12 + 0xa = 0x120a
			y = (int(header[x * 2], 16) << 8 | int(header[x * 2 + 1], 16))
			y = hex(y)
			total += int(y, 16)
		binary_check = ''
		for x in hex(total)[2:]:
			num_of_bits = 4
			binary_check += bin(int(x,16))[2:].zfill(num_of_bits)
		# convert to each hex into binary and concatanate
		continue_carry = True if len(binary_check) > 16 else False
		while continue_carry:
			# the bits left over from the truncating the last 16 bits are added to the 16 bits, if there are any
			# if generation of binary length > 16 then we have to carry until len of binary == 16
			bit_carry = binary_check[:len(binary_check) - 16]
			bit_remain = binary_check[len(bit_carry):]
			binary_check = bin(int(bit_carry, 2) + int(bit_remain, 2))[2:].zfill(16)
			continue_carry = True if len(binary_check) > 16 else False
		cs_binary_invert = ''
		for x in binary_check:
			# flip every bit, dont know how to implement the ~ operator which should flip bits
			if x == '0':
				cs_binary_invert += '1'
			else:
				cs_binary_invert += '0'
		new_hex_cs = ''
		for x in xrange(len(cs_binary_invert[::4])):
			index = x * 4
			new_hex_cs += hex(int(cs_binary_invert[index:index + 4],2))[2:]
		return new_hex_cs


	def validate_checksum(self, header=None):
		if header == None:
			header = self.iphl
		total = 0
		for x in xrange(len(header[::2])):
			# Takes 1 byte and concatenates it to the next byte via bit shifting
			# e.g., 0x12 + 0xa = 0x120a
			y = (int(header[x * 2], 16) << 8 | int(header[x * 2 + 1], 16))
			total += y
		total = hex(total)
		total = int(total[2], 16) + int(total[3:], 16)
			# carries first hex value and adds it to the remaining value. Should equal ffff
			# e.g., 3fffc; 3 + fffc = ffff
		if hex(total).lower() == '0xffff':
			return True
		else:
			return False

# with open(sys.argv[1],'r') as input_file:
with open("F:\\Coding\\Code Eval\\test_data", 'r') as input_file:
	for x in input_file.read().split('\n'):
		new_sip = x.split()[0]
		new_dip = x.split()[1]
		hex_packet = x.split()[2:]
		package = packet(hex_packet)
		new_ip_header = package.change_IPs(new_sip, new_dip)
		sys.stdout.write( new_ip_header + '\n' )
