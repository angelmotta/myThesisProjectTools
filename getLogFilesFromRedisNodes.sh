#!/bin/bash
docker cp redis_svr1:/root/mylogs/redissvr1.log logs/sinrabia/t_sample_5000_2/
docker cp redis_svr2:/root/mylogs/redissvr2.log logs/sinrabia/t_sample_5000_2/
docker cp redis_svr3:/root/mylogs/redissvr3.log logs/sinrabia/t_sample_5000_2/

# Monitor
# On svr1
# redis-cli -p 6380 monitor | tee redissvr1.log

# On svr2
# redis-cli -p 6381 monitor | tee redissvr2.log

# On svr3
# redis-cli -p 6382 monitor | tee redissvr3.log