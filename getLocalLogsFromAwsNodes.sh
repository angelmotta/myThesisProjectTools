#!/bin/bash
mkdir -p ~/mylogs/t23052023_1301
mkdir -p ~/mylogs/t23052023_1301/svr1
mkdir -p ~/mylogs/t23052023_1301/svr2
mkdir -p ~/mylogs/t23052023_1301/svr3
mkdir -p ~/mylogs/t23052023_1301/cli1
mkdir -p ~/mylogs/t23052023_1301/cli2

cd /root/go/src/rabia/deployment/install
# Get Redis Monitor Logs
cp /root/redis-6.2.2/rabiasvr1log.txt /root/mylogs/t23052023_1301/
scp -i id_rsa root@rabiasvr2:/root/redis-6.2.2/rabiasvr2log.txt /root/mylogs/t23052023_1301/
scp -i id_rsa root@rabiasvr3:/root/redis-6.2.2/rabiasvr3log.txt /root/mylogs/t23052023_1301/

# Get Rabia Logs
cp /root/go/src/rabia/logs/* /root/mylogs/t23052023_1301/svr1/
scp -i id_rsa root@rabiasvr2:/root/go/src/rabia/logs/* /root/mylogs/t23052023_1301/svr2/
scp -i id_rsa root@rabiasvr3:/root/go/src/rabia/logs/* /root/mylogs/t23052023_1301/svr3/
scp -i id_rsa root@rabiacli1:/root/go/src/rabia/logs/* /root/mylogs/t23052023_1301/cli1/
scp -i id_rsa root@rabiacli2:/root/go/src/rabia/logs/* /root/mylogs/t23052023_1301/cli2/

# Tar directory
cd ~/mylogs/
tar czvf t23052023_1301.tar.gz t23052023_1301/
cp t23052023_1301.tar.gz /home/ubuntu
