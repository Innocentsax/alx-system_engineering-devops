# Web infrastructure design

![web_structure](https://media.geeksforgeeks.org/wp-content/uploads/20220817182651/NetworkInfrastructure1.png)

Web Applications Infrastructure/Web Infrastructure also called internet infrastructure is the physical hardware, transmission media, and software used to interconnect computers and users on the Internet.

- Simple Web Infrastructure
- Distributed Web Infrastructure
- Monitored Web Infrastructure

## Learning Objectives

- You must be able to draw a diagram covering the web stack you built with the `*sysadmin/devops*` track projects
- You must be able to explain what each component is doing
- You must be able to explain `system redundancy`
- Know all the mentioned acronyms: `LAMP`, `SPOF`, `QPS`


## Simple Web Infrastructure

![](https://miro.medium.com/max/720/1*xKd1CchSaSKV83Oizju8kg.webp)

- 1 server
- 1 web server `(Nginx)`
- 1 application server
- 1 application files (your code base)
- 1 database `(MySQL)`
- 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`

## Distrubuted Web Infrasture

![](https://upload.wikimedia.org/wikipedia/commons/5/55/Network_Architecture_Diagram_-_Distributed_Web_Infrastructure.pdf)

- 2 servers
- 1 web server `(Nginx)`
- 1 application server
- 1 load-balancer `(HAproxy)`
- 1 set of application files (your code base)
- 1 database `(MySQL)`

## Monitored web infrastructure

![](https://miro.medium.com/max/720/1*t7oSAWV7gtp-WSRNXfM9Hw.webp)

- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)
