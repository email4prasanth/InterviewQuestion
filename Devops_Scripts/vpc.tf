terraform{
    required_providers{
        aws = {
            source = "hashicorp/aws"
            version = "~>5.0"
        }
    }
}

provider "aws" {
    region =var.aws_region
}

resource "aws_vpc" "vpc"{
    cidr_block =  var.vpc_cidr
    tags =  {
        Name = "${var.ec2_name}-VPC"
    }
}
resource "aws_subnet" "public_subnet"{
    vpc_id = aws_vpc.vpc.id
    count = length(var.public_subnet_cidr)
    cidr_block = element(var.public_subnet_cidr, count.index)
    tags = {
        Name = "${var.ec2_name}-public-subnet-${count.index+1}"
    }
}
resource "aws_subnet" "private_subent" {
    vpc_id = aws_vpc.vpc.id
    count = length(var.private_subent_cidr)
    cidr_block = element(var.private_subent_cidr, count.index+1)
    tags = {
        Name = "${var.ec2_name}-private-subent-${count.index+1}"
    }
}
resource "aws_internet_gateway" "igw" {
    vpc_id = aws_vpc.vpc.id
    tags = {
        Name = "${var.ec2_name}-igw"
    }
}
resource "aws_security_groups" "sg" {
    vpc_id = aws_vpc.vpc.id
    ingress {
        description = "allow ssh port"
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        description = 
        form_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}
resource "aws_routing_table" "pubrt" {
    vpc_id = aws_vpc.id
    route {
        cidr_block = ["0.0.0.0/0"]
        gateway_id = aws_internet_gateway.igw.id
    }
    tags = {
        Name = "${var.ec2_name}-RT"
    }
}
resource "aws_routing_table_association" "rtass" {
    count = length(var.public_subnet_cidr)
    subnet_id = element(var.public_subnet_cidr.*.id, count.index)
    rout_table_id = aws_routing_table.pubrt.id
}
resource "aws_instance" "web" {
    count = length(var.public_subnet_cidr)
    ami = "${var.ami_id}"
    instance_type = "t2.large"
    key_name = "DevOpsKey"
    subnet_id = element(var.public_subnet_cidr.*.id, count.index)
    vpc_security_group_ids = ["${aws_security_groups.sg.id}"]
    associate_public_ip_address = true 
    tags = {
        Name = "${var.ec2_name}-pubic-server-${count.index+1}"
    }
}

### variable.tf
variable "aws_region" {}
variable "vpc_cidr" {}
variable "ec2_name" {}
variable "public_subnet_cidr" {}
variable "private_subent_cidr" {}
variable "ami_id" {}

#### terraform.tfvars
aws_region = "ap-south-1"
vpc_cidr = ["10.1.0.0/16"]
ec2_name = "dkutti"
public_subnet_cidr = ["10.1.1.0/24","10.1.2.0/24","10.1.3.0/24"]
private_subent_cidr = ["10.1.10.0/24","10.1.20.0/24","10.1.30.0/24"]
ami_id = "ami-"