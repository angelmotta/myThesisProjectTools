#!/bin/bash
docker cp redis_svr1:/root/mylogs/redis_svr1.txt logs/sinrabia/
docker cp redis_svr2:/root/mylogs/redis_svr2.txt logs/sinrabia/

# Monitor
# On svr1
# redis-cli -p 6380 monitor | tee redis_svr1.txt

# On svr2
# redis-cli -p 6381 monitor | tee redis_svr2.txt
