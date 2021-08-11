# CICD pipeline to aws S3 & Elastic Beanstalk

#### CI part actions:
1. Git clone repo
2. Create zip deployment packege
3. Configure AWS credentials
4. Copy deployment package to S3 bucket
5. Print CD finish message

#### CD part actions:
1. Configure AWS credentials
2. Create new EB app version
3. Deploy new EB app version
4. Print CD finish message

