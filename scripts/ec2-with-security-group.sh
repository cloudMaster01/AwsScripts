#!/bin/bash

echo Enter the security group ID :

read sg_id

i=`aws ec2 describe-instances | egrep InstanceId | awk {'print $2'} | awk -F \\" {'print $2'} | sort -n | uniq | sort`

for instance in ${i[@]}
do
si=`aws ec2 describe-instances --instance-ids $instance | grep GroupId | awk {'print $2'} | awk -F \\" {'print $2'}| sort -n | uniq | sort`
for securitygroup in ${si[@]}
do
echo "For Instance $instance\\, the Security-Groups are: ${si[@]}" >> /tmp/$sg_id.txt
done
done

cat /tmp/$sg_id.txt | grep $sg_id
