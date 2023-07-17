# Firewall

<img src="https://www.compuquip.com/hs-fs/hubfs/images/blog-images/firewall-monitoring-best-practices.jpg?width=600&name=firewall-monitoring-best-practices.jpg" width="1000" height="250">

> A firewall is a network security device that monitors incoming and outgoing network traffic and permits or blocks data packets based on a set of security rules. Its purpose is to establish a barrier between your internal network (LAN) and incoming traffic from external sources (such as the internet) in order to block malicious traffic like viruses and hackers.

## The UFW On Linux Distro

<img src="https://codedesign.fr/wp-content/uploads/2018/08/ubuntu-ufw-1-880x276.png" width="1500" height="250">

The __Uncomplicated firewall (UFW)__ in my ubuntu 22.04 LTS comes preinstalled but disabled, i only needed to enable it to get going. However lets take note of the following:

* Once __UFW__ is enabled you have to set the rules on that terminal session especially when you're connecting via ssh cause by default ufw blocks all connection to port 22.
* __UFW__ doesn't have a native port forwarding command, you need to do it via its `/etc/ufw/before.rules` file
* You also need to enable port forwarding by uncommenting the `net.ipv4.ip_forward=1` line in `/etc/sysctl.conf`
* 

### Code on Terminal

```bash
# check if ufw is installed or enabled
$ sudo ufw status

# if the result shows enabled then disable it
$ sudo ufw disable

# configuring firwall rules
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22/tcp		/to enable ssh connection
$ sudo ufw allow 80/tcp		/to enable connection on port 80
$ sudo ufw allow 443/tcp	/to enable conection on port 443
$ sudo ufw enable

# enabling port forwarding via UFW

# add this below rule to the /etc/ufw/before.rules file
# make sure its before the *filter line, VERY IMPORTANT

*nat
: PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT

# Then go to your /etc/sysctl.conf file to enable port forwarding by
# uncommenting the line #net.ipv4.ip_forward=1

-- before
#net.ipv4.ip_forward=1

--after
net.ipv4.ip_forward=1

# then reload the sysctl configuration
$ sudo sysctl -p

# congratulations !! you've done it
# if this is confusing, then watch the video above to get it done yourself.
```

## Author
#### ___[UDO INNOCENT CHARLES](https://github.com/Innocentsax)___
