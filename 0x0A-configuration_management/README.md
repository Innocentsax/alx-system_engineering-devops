# Configuration management

![configuration_management](https://wac-cdn.atlassian.com/dam/jcr:f4635478-48a1-45d1-9b2f-43d14b2666ba/Configuration-management-tools-2x.png?cdnVersion=690)

> Configuration management is a systems engineering process for establishing consistency of a product’s attributes throughout its life.

Puppet is a tool that helps you manage and automate the configuration of servers. When you use Puppet, you define the desired state of the systems in your infrastructure that you want to manage.

![puppet](https://miro.medium.com/max/720/1*j0RHN3oXzOfXWl7XeLzxZw.webp)

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

## Project Requirements

- All your files will be interpreted on `Ubuntu 20.04 LTS`
- All your files should end with a new line
- A __README.md__ file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass `puppet-lint version 2.1.1` without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line __must be a comment__ explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension __.pp__

## Installing puppet and puppet-lint on ubuntu

### A video says it all
__Watch the video below to get a full grasp about tackling the project__

_Click the play video to watch video_ [Play video](https://youtu.be/YJyzEnXSsc8)

### Commands on Terminal
```bash

$ apt-get update && upgrade -y

$ sudo apt-get install -y ruby=1:2.7+1 --allow-downgrades

$ sudo apt-get install -y ruby-augeas

$ sudo apt-get install -y ruby-shadow

$ sudo apt-get install -y puppet

#installs puppet linter
$ gem install puppet-lint
```
__Follow the above instructions to install puppet and puppet-linter then watch the video to enable you understand how to get started with the task__
