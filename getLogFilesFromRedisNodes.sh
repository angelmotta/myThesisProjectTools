#!/bin/bash
docker cp redis_svr1:/root/mylogs/redislogsvr1.txt logs/sinrabia/t3/
docker cp redis_svr2:/root/mylogs/redislogsvr2.txt logs/sinrabia/t3/
docker cp redis_svr3:/root/mylogs/redislogsvr3.txt logs/sinrabia/t3/

# Monitor
# On svr1
# redis-cli -p 6380 monitor | tee redislogsvr1.txt

# On svr2
# redis-cli -p 6381 monitor | tee redislogsvr2.txt

# On svr3
# redis-cli -p 6382 monitor | tee redislogsvr3.txt