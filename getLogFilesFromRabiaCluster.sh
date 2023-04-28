#!/bin/bash
docker cp rabiasvr1:/root/redis-6.2.2/rabiasvr1log.txt rabia/
docker cp rabiasvr2:/root/redis-6.2.2/rabiasvr2log.txt rabia/
docker cp rabiasvr3:/root/redis-6.2.2/rabiasvr3log.txt rabia/

# Start Redis on Rabia
# On svr0
#./src/redis-server --port 6379 --appendonly no --save "" --daemonize yes
#./src/redis-cli -p 6379

# On svr1
#./src/redis-server --port 6380 --appendonly no --save "" --daemonize yes
#./src/redis-cli -p 6380

# On svr2
#./src/redis-server --port 6381 --appendonly no --save "" --daemonize yes
#./src/redis-cli -p 6381

