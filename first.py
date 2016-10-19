from pyVim import connect
from pyVim.connect import SmartConnect, Disconnect 
import ssl

from pyVmomi import vim
from pyVmomi import vmodl
from pyVim.task import WaitForTask
import atexit
import sys

if __name__ == "__main__":
    
    s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    s.verify_mode = ssl.CERT_NONE
    c = SmartConnect(host="ip", user="user_name", pwd='password',  sslContext=s)
 
    print(c.CurrentTime()) 
   
   ### list vms on data center
#datacenter = c.content.rootFolder.childEntity[0]
#vms = datacenter.vmFolder.childEntity
 
#for i in vms:
#    print(i.name)

# find vm

searcher = c.content.searchIndex
vm1 = searcher.FindByIp(ip="172.16.225.48", vmSearch=True)
x = vm1.config.name
print vm1.config.name
print vm1
print vm1.config.uuid
xx = vm1.config.uuid
content = c.RetrieveContent()
#print content

vm = searcher.FindByUuid(None, xx, True)
print vm
vcpu_nu = 4


def change_vcpu(vm, c, vcpu_nu):
    vcpu_nu=int(vcpu_nu)
    cspec = vim.vm.ConfigSpec() 
    cspec.numCPUs = vcpu_nu
    cspec.numCoresPerSocket = 1 
    WaitForTask(vm.Reconfigure(cspec))
Disconnect(c)
