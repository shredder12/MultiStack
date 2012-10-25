from boto.ec2.connection import EC2Connection 
from boto.ec2.regioninfo import EC2RegionInfo

region_var = EC2RegionInfo(name="siel.openstack", endpoint="10.2.4.129:8773")
print region_var

conn = EC2Connection('demo', 'demo', region=region_var, is_secure=False, path="/services/Cloud")
print conn

#This a fixed image ID for our private cloud. Its ubuntu-12.04-amd64

default_image_id = "ami-00000010"

def connect_cloud(access_key, secret_key, url):
    '''
    Function: connect_cloud(access_key, secret_key, url)
    ----------------------------------------------------
    This function uses ec2 API to connect to various cloud providers.
    Note that, it only connects to one cloud at a time.
    
    @param access_key: The EC2 access key.
    @param secret_key: The EC2 secret key.
    @param url: The EC2 API endpoint of the cloud.
    
    @return: The connection descriptor.
    
    '''

def gen_save_keypair():
    '''
    Function: gen_save_keypair()
    ----------------------- 
    This function will generate a temporary keypair to be used by
    HadoopStack and save it in /tmp/HadoopStack directory.
    
    @return: bool: true or false, depicting success or failure respectively.
    
    @todo: Need to find a way to save this key securely. May be in per process
    tmp dir - /var/tmp/.
    
    '''
    
    key_pair = conn.create_key_pair("hadoopstack")
    key_pair.save("/tmp/HadoopStack")
    return True

def spawn_instances(number, flavor, keypair, region, image_id=default_image_id, sec_group):
    '''
    Function: spawn_instances(number, flavor)
    -----------------------------------
    This function spawns virtual machines.
    
    @param number: The number of virtual machines to boot.
    @param flavor: The flavor of virtual machine, e.g. - m1.small etc.
    @param keypair: SSH keypair to be associated with each instance.
    @param region: Region in which instance will be spawned.
    @param image: Image to be booted.
    @param sec_group: Security group the instances are going to be associated with.
    
    @return 
    
    '''
