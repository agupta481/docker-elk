#give folder names

folders = list({"payroll","accounting"})
instance = "dev-web01"
environment = "dev"

#powershell.exe -ExecutionPolicy UnRestricted -File .\install-service-filebeat.ps1
#
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('filebeat.j2')
output_from_parsed_template = template.render(folders=folders,instance=instance,environment=environment)
print(output_from_parsed_template)

# to save the results
with open("filebeat.yml", "w") as fh:
    fh.write(output_from_parsed_template)