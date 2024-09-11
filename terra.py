
import subprocess

def terraform_run(command):
    process = subprocess.run(
        command, 
        shell=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    
    print(process.stdout.decode())
   
directory = r"A:\Python_DevOps\Python_workshop\terra-automate\Wanderlust-Mega-Project\terraform"
#command = f"terraform -chdir={directory} init"
#command = f"terraform -chdir={directory} plan"
command = f"terraform -chdir={directory} apply -auto-approve"
terraform_run(command)