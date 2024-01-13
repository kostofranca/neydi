d = {
    "bitbucket_prod":{"192.168.0.0":"9100",
                      "192.168.0.3":"9100"},
    "bitbucket_test":{"192.168.0.1":"9100"},
    "bitbucket_dmz":{"192.168.0.2":"9100"},
    "jenkins_test":{"192.168.0.3":"9100"}
}

for instance, address in d.items():
    for ip, port in address.items():
        config = f"""  
		- job_name: "{instance}"
			static_configs:
			- targets: ["{address.keys()}:{address.values()}"]
	"""
        print(config)
