d = {
    "bitbucket_prod":{"192.168.0.0":"9100"},
    "bitbucket_test":{"192.168.0.1":"9100"},
    "bitbucket_dmz":{"192.168.0.2":"9100"},
    "jenkins_test":{"192.168.0.3":"9100"}
}

def create_yml(path, data):

	with open(path, "w") as f:

		for instance,address in data.items():
			config = f"""  
		- job_name: "{instance}"
			static_configs:
			- targets: ["{address.keys()}:{address.values()}"]
	"""
			f.writelines(config)

	print("prmetheus initialized!")

create_yml("prometheus.yml", d)

# Read yml and create a json of scrape_configs

# Create prometheus.yml

# Check if there are new entries

# Update prometheus.yml add and delete.

