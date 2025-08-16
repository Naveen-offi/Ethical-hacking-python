import subprocess

new_mac = "00:00:07:a1:c2:b3"
interface = "eth0"

print("Shuting down Network...")
subprocess.run(["ifconfig", interface ,"down"])

print(f"Changing Mac Address to {new_mac}")
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])

print(f"Successfull Changed Mac Address")
  
print(f"Turning On ifconfig")
subprocess.run(["ifconfig", interface, "up"])

subprocess.run(["ifconfig"])

