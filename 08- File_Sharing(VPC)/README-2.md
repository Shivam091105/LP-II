# Secure File Sharing Between Cloud Instances using AWS EC2

## Objective

To create a secure cloud environment where two EC2 virtual machines communicate within a private virtual network and securely transfer files using SCP (Secure Copy Protocol) with proper access permissions.

---

# Technologies Used

* Amazon Web Services
* Amazon EC2
* Amazon VPC
* Ubuntu Linux
* SSH
* SCP

---

# Architecture

The setup contains:

* One custom VPC
* Two Ubuntu EC2 instances
* Secure communication using private IPs
* File transfer using SCP over SSH

---

# Prerequisites

Before starting, ensure you have:

* AWS Account
* Basic Linux terminal knowledge
* SSH Key Pair (.pem file)
* Internet connection

---

# Step 1: Create a VPC

1. Login to [AWS Console](https://aws.amazon.com/console/?utm_source=chatgpt.com)
2. Open **VPC Dashboard**
3. Click **Create VPC**

Configuration:

| Setting   | Value       |
| --------- | ----------- |
| Name      | project-vpc |
| IPv4 CIDR | 10.0.0.0/16 |

Click **Create VPC**

---

# Step 2: Create Subnets

Create two subnets inside the VPC.

| Subnet          | CIDR         |
| --------------- | ------------ |
| Public Subnet 1 | 10.0.24.0/24 |
| Public Subnet 2 | 10.0.25.0/24 |

---

# Step 3: Create Security Group

Create one security group and attach it to both EC2 instances.

Add the following inbound rules:

| Type            | Protocol | Port | Source      |
| --------------- | -------- | ---- | ----------- |
| SSH             | TCP      | 22   | Your IP     |
| SSH             | TCP      | 22   | 10.0.0.0/16 |
| All ICMP - IPv4 | ICMP     | All  | 10.0.0.0/16 |

Purpose:

* SSH rule allows secure login
* ICMP rule allows ping communication

---

# Step 4: Launch Two EC2 Instances

Launch two Ubuntu EC2 instances.

Configuration:

| Setting        | Value         |
| -------------- | ------------- |
| AMI            | Ubuntu Server |
| Instance Type  | t2.micro      |
| VPC            | project-vpc   |
| Security Group | Created SG    |
| Key Pair       | mykey.pem     |

Instance Names:

| Instance | Purpose  |
| -------- | -------- |
| VM1      | Receiver |
| VM2      | Sender   |

---

# Step 5: Connect to Both Instances

From local terminal:

## Connect to VM1

```bash id="9sh8kt"
ssh -i mykey.pem ubuntu@<VM1-Public-IP>
```

## Connect to VM2

```bash id="x7yr1w"
ssh -i mykey.pem ubuntu@<VM2-Public-IP>
```

---

# Step 6: Verify Private Network Communication

From VM2:

```bash id="ml62to"
ping <VM1-Private-IP>
```

Example:

```bash id="u3lgzx"
ping 10.0.24.153
```

Expected Output:

```text id="x4twgo"
64 bytes from 10.0.24.153
```

Press:

```bash id="hynw0f"
Ctrl + C
```

to stop ping.

---

# Step 7: Create a Sample File

Inside VM2:

```bash id="j0ysqf"
echo "Secure Cloud File Sharing" > sample.txt
```

Check file contents:

```bash id="up1pji"
cat sample.txt
```

Output:

```text id="s8qk5k"
Secure Cloud File Sharing
```

---

# Step 8: Copy PEM Key to VM2

From your local machine:

```bash id="o1mx7l"
scp -i mykey.pem mykey.pem ubuntu@<VM2-Public-IP>:/home/ubuntu/
```

---

# Step 9: Set Proper Key Permissions

Inside VM2:

```bash id="qqs1vh"
chmod 400 mykey.pem
```

---

# Step 10: Transfer File Securely using SCP

From VM2:

```bash id="8hrrv7"
scp -i mykey.pem sample.txt ubuntu@<VM1-Private-IP>:/home/ubuntu/
```

Example:

```bash id="v2j2oz"
scp -i mykey.pem sample.txt ubuntu@10.0.24.153:/home/ubuntu/
```

---

# Step 11: Verify File on VM1

Login to VM1 and run:

```bash id="vm2f4p"
ls
```

Then:

```bash id="7nt1w5"
cat sample.txt
```

Expected Output:

```text id="b8gr4z"
Secure Cloud File Sharing
```

---

# Step 12: Apply Secure File Permissions

Inside VM1:

```bash id="zq8r2z"
chmod 600 sample.txt
```

Check permissions:

```bash id="76j1t2"
ls -l
```

Expected Output:

```text id="kce51z"
-rw------- 1 ubuntu ubuntu sample.txt
```

Meaning:

* Owner has read/write access
* Group has no access
* Others have no access

---

# Security Features Implemented

✔ Secure VPC communication
✔ SSH-based authentication
✔ SCP secure file transfer
✔ Restricted Security Group access
✔ Linux file permission control
✔ Private IP communication

---

# Common Errors and Solutions

## Error 1

```text id="t0k8rq"
No route to host
```

### Solution

* Check Security Group rules
* Allow ICMP and SSH traffic
* Verify correct private IP

---

## Error 2

```text id="w7gyqm"
Permission denied (publickey)
```

### Solution

Use PEM key during SCP:

```bash id="sd6p8j"
scp -i mykey.pem sample.txt ubuntu@<Private-IP>:/home/ubuntu/
```

---

# Result

Successfully created a secure cloud-based environment where two EC2 virtual machines communicate securely within a VPC and transfer files using SCP with proper access permissions.

---

# Advantages

* Secure communication
* Fast internal file transfer
* Scalable cloud setup
* Access-controlled sharing
* Cost-effective implementation

---

# Viva Questions

## 1. What is a VPC?

A VPC (Virtual Private Cloud) is a logically isolated network in AWS.

---

## 2. What is SCP?

SCP (Secure Copy Protocol) securely transfers files using SSH.

---

## 3. Why are private IPs used?

Private IPs provide secure internal communication inside the VPC.

---

## 4. What is the role of Security Groups?

Security Groups act as virtual firewalls controlling network traffic.

---

## 5. What does chmod 600 mean?

600 = 4+2+0

* 6 → Read + Write for owner
* 0 → No permissions for group
* 0 → No permissions for others
