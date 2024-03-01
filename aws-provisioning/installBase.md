# Provisioning EC2 Server instance using Rabia

## Provisioning Operating System and base dependencies

## OS Image used in AWS EC2 instances

OS Image: ubuntu-bionic-18.04-amd64-server-20230323

## Notes for MacOS / Linux

Once servers are installed we can register the Vms's public
IPs (EC2) on our local development machine.

```bash
sudo vim /etc/hosts
dscacheutil -flushcache
```

## Change hostname

```bash
sudo su -
hostnamectl set-hostname <rabiasvr1>
```

## Installing packages

```bash
apt-get update && apt-get install -y \
  git \
  vim \
  wget \
  sudo \
  inetutils-ping \
  iproute2 \
  openssh-server \
  net-tools \
  telnet
```

## Installing Rabia

## 1. Download the project to the default path in the server

```bash
mkdir -p ~/go/src && cd ~/go/src
git clone https://github.com/angelmotta/rabia.git
cd rabia
git checkout test-rabia
```

## 2. Install Rabia and its dependencies

```bash
cd deployment
. ./install/install.sh
```

## 3. Test installation in each node

```bash
cd ./run
. single.sh          # the default parameter runs a Rabia cluster on a single machine for 20 seconds
cat ../../result.txt # inspect the performance statistics; one should see a few lines of file output
. clear.sh           # remove logs, result.txt, and the built binary
```

## 5. Configure Rabia Cluster

From server1 send the profile configuration file to other servers/clients in the cluster

```bash
cd ~/go/src/rabia/deployment/install
scp -i id_rsa ../profile/profile0.sh root@rabiasvr2:/root/go/src/rabia/deployment/profile/
scp -i id_rsa ../profile/profile0.sh root@rabiasvr3:/root/go/src/rabia/deployment/profile/
scp -i id_rsa ../profile/profile0.sh root@rabiacli1:/root/go/src/rabia/deployment/profile/
scp -i id_rsa ../profile/profile0.sh root@rabiacli2:/root/go/src/rabia/deployment/profile/
```

# 6. Execute Test Rabia Cluster

```bash
cd ~/go/src/rabia/deployment/run
. multiple.sh
cat ../../result.txt  # check logs
```

# 7. Enable storage mode to use Redis on replica (rabiasvr1)

In Rabia implementation code, it is enough to do this change only on replica 1.

```bash
cd ~/go/src
vim rabia/internal/config/config.go
c.StorageMode = 0     # Change to 1 to Redis
c.RedisAddr = []string{"localhost:6379", "localhost:6380", "localhost:6381"}
```

Note that we are using `localhost:` so there is no communication between Redis instances. Rabia provides the communication layer between nodes.

# 8. Start Redis instances in stand-alone mode

On each replica start Redis instance in stand-alone mode and start `Monitor` tool to register database operations to a `log file`.

On Replica 1

```bash
cd ~/redis-6.2.2/
src/redis-server --port 6379 --appendonly no --save "" --daemonize yes
src/redis-cli -p 6379 MONITOR | tee rabiasvr1log.txt
```

On Replica 2

```bash
cd ~/redis-6.2.2/
src/redis-server --port 6380 --appendonly no --save "" --daemonize yes
src/redis-cli -p 6380 MONITOR | tee rabiasvr2log.txt
```

On Replica 3

```bash
cd ~/redis-6.2.2/
src/redis-server --port 6381 --appendonly no --save "" --daemonize yes
src/redis-cli -p 6381 MONITOR | tee rabiasvr3log.txt
```
