- Packer is used to create AMI (Amazon Machine Image) which is a static Artifacts
    - Build - It is a single task that produces artifacts
    - Artifacts - This is result of a single build, Every builder produces artifacts.
    - Provisioners - It is set of code that execute berfore creating AMI that can install software using shell script, chef, puppet
    - Builder - Components of packer that ead the information given and creates Machine image like VMware.
    - Datasources - fetch data from outside of packer to use in template. Amazon AMI, AmazonSecreteManger
    - post-processor - create a new arifacts.
    - Template - (hcl or json) packer able to read template and create multiple machines paralelly.
- https://developer.hashicorp.com/packer/docs/templates/legacy_json_templates/user-variables

#### packer syntax:
{
  "_comment": "This is a comment",
  "variables":{},
  "builders": [{}],
  "provisioners":[{}]
}
#### variable sytax
"variables":{
      "aws_access_key": "",
      "aws_secret_key": "",
      "region": ""
 }
#### builder syntax
"builders": [
    {
        "_comment":"Decleared in varaible section"
        "access_key": "{{user `aws_access_key`}}",
        "secret_key": "{{user `aws_secret_key`}}",
        "region": "{{user `region `}}"

    }]