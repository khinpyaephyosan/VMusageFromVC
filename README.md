VMusageFromVC
=============

To report Virutal Machine Usage Information from vCenter Server to administrator or other autorized person.   

Requirements
------------

vsphere python SDK need to install. (link: https://github.com/vmware/vsphere-automation-sdk-python)

Role Variables
--------------   

You can customize varialbles under vars/main.yml ! You need to define vcenter username and password in defaults/main.yml. later you can use vault file under defaults/vault.yml then encrypt it.   

reporter: exampleuser@exampledomain.com   
subject: 'VM utilization report from vCenter Servers'   
body: 'This is VM utilization report from vCenter Servers!'   
smtp_host: 'hostname or ip address of local smtp server'
smtp_port: 'smtp port number'

vcenter server host, username and password. (ps: ready only credential is OKAY)   
ip: 'x.x.x.x'   
username: 'example@vsphere.local'   
password: 'example password'   
   
Example Playbook
----------------

./monitorvc.yml


Author Information
------------------

https://about.me/lillianphyoe
