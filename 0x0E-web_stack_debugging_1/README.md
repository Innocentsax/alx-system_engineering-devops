# 0x0E Web stack debugging #1 :wrench:

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCr1U_4zHjKIB1fqzw6Ce5JTqDLoeCBWLW5w&usqp=CAU" width="1000" height="280">

> Debugging is the process of finding and fixing errors in software that prevents it from running correctly. As you become a more advanced programmer and an industry engineer, you will learn how to use debugging tools such as gdb or built-in tools that IDEs have. However, it’s important to understand the concepts and processes of debugging manually. This project covers a second part of the optimal framework and blueprint for debugging web stack (remote containers this scenario) bugs

Challenge:

Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue.

## A Video to explain it all
__Watch the video to see how i was able to come up with the solutions to the task.__

__Click the "watch video" to play video__ [__watch video__](https://youtu.be/Fx6ewkKQdU0)

## Tasks :heavy_check_mark:

0. Bash script with the minimum number of commands to automate your fix.
1. Bash script with the minimum number of commands to automate your fix. v2


## Results :chart_with_upwards_trend:

| Filename |
| ------ |
| [0-nginx_likes_port_80](./0-nginx_likes_port_80)|
| [1-debugging_made_short](./1-debugging_made_short)|

## Additional info :construction:

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 20.04 LTS`
- All your files should end with a new line
- A __README.md file__ at the root of the folder of the project is mandatory
- All your __Bash script files must be executable__
- Your Bash __scripts must pass Shellcheck__ without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- You are not allowed to use `wget`

### Resources

- BASH
- Debian 9 stable / Ubuntu 16.04 / Ubuntu 18.04 
- Shellcheck
- Docker
- Webstack debugging
- Networking Basics

### Try It On Your Machine :computer:

```bash
git clone https://github.com/sammykingx/alx-system_engineering-devops.git
cd 0x0E-web_stack_debugging_1
cat FILENAME
curl 0:80
cat -e FILENAME | wc -l
curl 0:80
```
