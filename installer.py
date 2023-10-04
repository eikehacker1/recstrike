import os 
import time 


print("instalando GO")

os.system(f"sudo apt install -y  golang")

time.sleep(0.5)
#instalando ferramentas feitas em go

os.system(f"go install -v github.com/lc/gau/v2/cmd/gau@latest")
os.system(f"go install -v github.com/tomnomnom/gf@latest")
os.system(f"go install -v github.com/ferreiraklet/airixss@latest")
os.system(f"go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@lates")
os.system(f"go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest")
os.system(f"go install -v github.com/tomnomnom/meg@latest")
os.system(f"go install -v github.com/tomnomnom/assetfinder@latest")
os.system(f"go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
os.system(f"go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest")
os.system(f"go install github.com/tomnomnom/qsreplace@latest")
time.sleep(0.5)
os.system(f"cp /root/go/bin/*  /usr/bin")

print("ferramentas em go instaladas [**!!]")

os.system(f"sudo apt install -y amass")

print("configurando")

os.system(f"mkdir ~/.gf")

os.system(f"git clone https://github.com/1ndianl33t/Gf-Patterns.git")


os.system(f"cp Gf-Patterns/*.json  ~/.gf")

