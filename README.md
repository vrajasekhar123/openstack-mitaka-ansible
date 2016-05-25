# Openstack-Mitaka_With-Ansible
Openstack Mitaka With Ansible
#Prerequisites:-
One node with Ansible installed. (You can use ansible in any one of openstack nodes or in separate node)
2 nodes with below configurations.

i. VM1(Controller) - Hard disk 50GB, RAM 4 GB, 1 CPU, Interfaces 3 ( 1 NAT, 2 Host only adapter vboxnet0 )

ii. VM2(Compute) - Hard disk 50GB, RAM 2 GB, 2 CPU, Interfaces 3 (1 NAT, 2 Host only adapter vboxnet0 )

All 2 VMs should communicate with each other and with ansible node.

#How to use :-
Copy the attached to your ansible node and untar the same.
Here you have to edit the 2 basic files.                     
i. inventory/hosts :- Host file to ansible 
ii. group_vars/all:- Var file to define IPs, user names and passwords.
And you can simple install the OpenStack with single command from openstack_main.yml file location.

#command:
ansible-playbook -i inventory/ openstack_main.yml
