def create_yml(path, data):

	with open(path, "w") as f:

		for instance,address in data.items():
			config = f"""  
		- job_name: "{instance}"
			static_configs:
			- targets: ["{address}:9100"]
	"""
			f.writelines(config)

	print("prmetheus initialized!")