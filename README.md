# Github Actions: CICD pipeline of Flask app to AWS S3 & Elastic Beanstalk

#### on AWS:
1. Create AWS IAM user with programmatic access, create Access Key and Secret Key
2. Add EB and S3 read/write policies to IAM user
3. Create AWS S3 Bucket
4. Create Flask environment on EB

#### on Github:
1. Create repository
2. Add secrets
3. Create workflow
4. Exclude .github folder

## Github Actions script steps

#### CI part steps:
1. Git clone repo
2. Create zip deployment packege
3. Configure AWS credentials
4. Copy deployment package to S3 bucket
5. Print CD finish message

#### CD part steps:
1. Configure AWS credentials
2. Create new EB app version
3. Deploy new EB app version
4. Print CD finish message

