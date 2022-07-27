In order to upload builds and collect statistics we run Ubuntu server with docker.

## Create new user
First a new local user must be created:
~~~
sudo useradd -m -d /home_local/electron electron
sudo passwd electron
sudo usermod -aG sudo electron
su - electron
~~~


## Install git
~~~
sudo apt install git
~~~

## Install Docker
Instruction is taken from: https://docs.docker.com/engine/install/ubuntu/
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
    
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

```

start and enable docker service
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

install docker-compose
```bash
sudo yum install -y docker-compose
```

## Start Docker
First, set following environment variables for your user (electron user) 
  - client_id
  - client_secret

How to get values you can read in [upload_to_SharePoint.md](upload_to_SharePoint.md).

Second,
create folder "settings" in the same dir with [docker-compose.yml](../docker/docker-compose.yml) 
file and put there downloader config files.

Finally,
start docker services via
```bash
sudo -E docker-compose up -d
```
This will start docker compose, pass environment variables from current user and detach from docker.
