VMusageFromVC
=============

To run python script which fetch VM resource utilization from vCenter server and generate csv file. At final, have to sent report to administration for decision making process.

Requirements
------------

vsphere python SDK need to install. (link: https://github.com/vmware/vsphere-automation-sdk-python)

Role Variables
--------------   

You can customize varialbles under vars/main.yml ! You need to define vcenter username and password in defaults/main.yml. later you can use vault file under defaults/vault.yml then encrypt it.   

reporter: exampleuser@exampledomain.com   
subject: 'VM utilization report from vCenter Servers'   
body: 'This is VM utilization report from vCenter Servers!'   

uip: 'x.x.x.x'   
uusername: 'example@vsphere.local'   
upassword: 'example password'   

pip: 'x.x.x.x'   
pusername: 'example@vsphere.local'   
ppassword: 'example password'   

Example Playbook
----------------

./monitorvc.yml

License
-------

BSD

Author Information
------------------

https://about.me/lillianphyoe
