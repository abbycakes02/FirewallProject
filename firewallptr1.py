#Firewall simulator project

#Firewall is found in-between an internal network and untrusted external network and the firewall monitors the traffic only allowing traffic that is allowed based on a set of pre-determined rules either you can block the traffic hence dropping the data packets or allow it into the internal network. 

#1. Create a python dictionary to set up a list of rules
#    1. The dictionary has key value pairs with the ip address mapped to the action taken so blocked or not 
#2. Create a function to generate a list of random ip numbers to simulate network traffic
#3. Then for each ip based on the set of rules, we can allow or block
#4. Output the result for each ip

import random 

def generate_random_IP():
	return(f"192.168.1.{random.randint(0,20)}")

def check_firewall_rules (ip_address, firewall_rules):
	for rule_ip, action in firewall_rules.items():
		if ip_address == rule_ip:
			return action 
	return "allow"
 	

def main():
		# create a dictionary of blocked ip addresses
		firewall_rules = {
		    "192.168.1.1": "block" ,
			"192.168.1.2": "block"
        }
		for i in range(12):
			ip_address = generate_random_IP()
			action = check_firewall_rules(ip_address, firewall_rules)
			random_number = random.randint(0,999)
	        # this number is a unique identifier to see 
			print(f"IP: {ip_address}, Action: {action}, Unique_id: {random_number}")

if __name__ == "__main__":
    main()
