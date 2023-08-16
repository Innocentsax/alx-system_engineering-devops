# Web_stack_debugging_4

![](https://media.geeksforgeeks.org/wp-content/uploads/20190902105053/Debugging-Tips-To-Get-Better-At-It.png)

## General Requirements

- All your files will be interpreted on `Ubuntu 14.04 LTS`
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass `puppet-lint version 2.1.1` without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension `.pp`
- Files will be checked with `Puppet v3.4`

### Task 0

```bash

root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   0.353 seconds
Complete requests:      2000
Failed requests:        943
   (Connect: 0, Receive: 0, Length: 943, Exceptions: 0)
Non-2xx responses:      1057
Total transferred:      1196526 bytes
HTML transferred:       789573 bytes
Requests per second:    5664.01 [#/sec] (mean)
Time per request:       17.655 [ms] (mean)
Time per request:       0.177 [ms] (mean, across all concurrent requests)
Transfer rate:          3309.15 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.1      0       8
Processing:     2   17   3.8     17      24
Waiting:        2   17   3.8     17      24
Total:          9   17   3.3     17      24

Percentage of the requests served within a certain time (ms)
  50%     17
  66%     19
  75%     20
  80%     20
  90%     21
  95%     23
  98%     23
  99%     23
 100%     24 (longest request)
root@0a62aa706eb3:/#
root@0a62aa706eb3:/# puppet apply 0-the_sky_is_the_limit_not.pp
Notice: Compiled catalog for 0a62aa706eb3.local in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[fix--for-nginx]/returns: executed successfully
Notice: Finished catalog run in 1.12 seconds
root@0a62aa706eb3:/#

----------- after fixing the issue ------------

root@0a62aa706eb3:/#
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      100
Time taken for tests:   2.405 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      1706000 bytes
HTML transferred:       1224000 bytes
Requests per second:    831.46 [#/sec] (mean)
Time per request:       120.271 [ms] (mean)
Time per request:       1.203 [ms] (mean, across all concurrent requests)
Transfer rate:          692.61 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   19  36.9      2     103
Processing:     1  101  63.2     98     398
Waiting:        1   95  62.3     97     296
Total:          3  120  53.7    101     399

Percentage of the requests served within a certain time (ms)
  50%    101
  66%    102
  75%    195
  80%    197
  90%    199
  95%    200
  98%    201
  99%    201
 100%    399 (longest request)

root@0a62aa706eb3:/#
```
> The issue was the maximum number of file nginx can open which was 15 so i just had to increase the number to a high amount.

### Task 1
- Resource [Read this](https://www.cyberciti.biz/faq/linux-unix-nginx-too-many-open-files/)

```bash

root@94091d11a274:/# su - holberton
-su: /etc/profile: Too many open files
-su: /home/holberton/.bash_profile: Too many open files
-su-4.3$
-su-4.3$ ls
-su: start_pipeline: pgrp pipe: Too many open files
-su-4.3$ exit
logout
-su: /home/holberton/.bash_logout: Too many open files
-su: /etc/bash.bash_logout: Too many open files

------- after fixing the error --------------------
root@94091d11a274:/# sudo vi /etc/security/limits.conf
root@94091d11a274:/# sudo sysctl -p
root@94091d11a274:/# su - holberton
holberton@94091d11a274:~$ ls
holberton@94091d11a274:~$ ls /
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
holberton@94091d11a274:~$
```
> The issue was the number of file the user `holberton` was allowed to open as you notice from my terminal i opened the file `/etc/security/limits.conf` to increase the size and that was how i was able to solve it.
__Never forget debugging starts from the error gotten___

Cheers.
