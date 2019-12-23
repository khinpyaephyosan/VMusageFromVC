from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl
import csv
import json
import sys 
import os
import datetime

date = datetime.datetime.now()
 
# Get all the Vms from vCenter server inventory and print its name
# Below is Python 2.7.x code, which can be easily converted to python 3.x version

s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode=ssl.CERT_NONE
si= SmartConnect(host=str(sys.argv[1]) , user=str(sys.argv[2]) , pwd=str(sys.argv[3]) ,sslContext=s)
content=si.content
 
# Method that populates objects of type vimtype
def get_all_objs(content, vimtype):
        obj = {}
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for managed_object_ref in container.view:
                obj.update({managed_object_ref: managed_object_ref.name})
        return obj
 
#Calling above method
getAllVms = get_all_objs(content, [vim.VirtualMachine])
cluster = get_all_objs(content, [vim.ClusterComputeResource])

filename = ""
for i in cluster:
     filename='report_'+cluster[i]+'_'+str(date)+'.csv'

path = "/home/srvmgmt/projects/python27/files/reports/"+filename

#if not os.path.exists(path):
#  os.makedirs(path)

header = ['IP','name','CPUs(count)','MEM(MB)','Provisioned(GB)','Used CPU(MHz)','Host MEM(MB)','Used MEM/Guest MEM(MB)','Used Storage(GB)','PowerState','freesapce on dir(MB)']
row = []
with open(path,'wt') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
#Iterating each vm object and printing its name
    for vm in getAllVms:
        row = []
        
        row.append(vm.summary.guest.ipAddress)
        row.append(vm.name)
        row.append(vm.summary.config.numCpu)
        row.append(vm.summary.config.memorySizeMB)
        row.append(vm.summary.storage.uncommitted/1024/1024/1024+vm.summary.storage.unshared/1024/1024/1024+1)

        #print "committed storage: "+str(vm.summary.storage.committed/1024/1024/1024)+" GB"

        #for i in vm.summary.vm.guest.disk:
        #   print i.diskPath+": "+str(i.freeSpace/1024/1024)+" MBps" # in MB's

        row.append(vm.summary.quickStats.overallCpuUsage)
        row.append(vm.summary.quickStats.hostMemoryUsage)
        row.append(vm.summary.quickStats.guestMemoryUsage)
        row.append(vm.summary.storage.committed/1024/1024/1024)
        
        row.append(vm.summary.runtime.powerState)
        
        path = "" 
        for i in vm.summary.vm.guest.disk:
           path+= str(i.diskPath)+" = "+str(i.freeSpace/1024/1024)+"MB ,"
        row.append(path)
        
        csv_writer.writerow(row)
        #$(echo "'IP','name','CPUs','MEM','Provisioned','Used CPU','Host MEM','Used MEM/Guest MEM','Used Storage'" >> output.csv)
        #$(echo "$ip,$name,$CPUs,$MEM,$Pstorage,$UCPU,$HMEM,$GMEM,$UStorage" >> output.csv)

        
