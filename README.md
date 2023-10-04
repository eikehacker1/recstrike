# recstrike
Um bot Para Automatizar Reconhecimento Em Aplicações WEB 

#### Esse script feito em python tem como objetivo automatizar e refinar o reconhecimento em aplicações WEB, usando ferramentas e utilitários feitos em GO.
#### AVISO: por favor !! De preferência use no KALI (WSL OU VM), ele pode demorar até algumas horas para terminar o processo, mas, isso não significa que alguns aqruivos de reconhecimento ainda não foram gerados.
#### Algumas coisas você terá que supervisionar manualmente.
#### POR FAVOR ESTEJA LOGADO EM USUÁRIO ROOT

# Instalação e configuração
```bash
sudo apt update && sudo apt upgrade
```
```bash
sudo apt install python3
```
```bash
sudo su
```
```bash
git clone https://github.com/eikehacker1/recstrike.git
```
```bash
cd recstrike 
```
```bash
chmod +x *.py  
```
```bash
python3 installer.py
```
#### Agora espere instalar e fique revisando se irá pedir alguma premissão para você

### Para executar:
``` bash
python3 bot.py <domínio_que_você_deseja.com>
```
### Note que é melhor você usar  ele de fora da sua pasta de reconhecimento:
```bash
python3 ~/recstrike/bot.py exemplo.com
```
### Isso pode deixar seu ambiente de reconhecimento menos sujo 
