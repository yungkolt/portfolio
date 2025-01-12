Cloud Resume Challenge with Serverless Architecture
This project combinines serverless architecture and cloud technologies to build a scalable and dynamic web resume.


Architecture diagram of the Cloud Resume

Features
Static Resume Website:

Hosted on an S3 bucket.
Delivered through a CloudFront distribution with custom domain integration.
Supports HTTPS with an ACM SSL certificate.
Visitor Counter:

Visitor count stored in a DynamoDB table.
Lambda function updates and retrieves the count dynamically.
Custom Domain:

Hosted on GoDaddy and integrated with CloudFront.
Serverless Backend:

AWS Lambda function processes API requests.
CloudFront forwards requests to the Lambda function.
Technologies Used
Frontend:

HTML/CSS/JavaScript for the resume.
Visitor counter dynamically displayed using JavaScript.
Backend:

AWS Lambda: Updates and retrieves the visitor count.
DynamoDB: Stores the visitor count.
CloudFront: Distributes the website globally with caching.
Infrastructure:

S3: Hosts the static resume.
GoDaddy: Manages the domain kolton.cloud.
ACM: Provides HTTPS certificates for secure access.
Architecture Diagram
Below is the architecture diagram of the Cloud Resume project:

graph LR
    A[User's Browser] -->|HTTPS Request| B[CloudFront Distribution]
    B -->|Static Content| C[S3 Bucket]
    B -->|API Request| D[AWS Lambda Function]
    D -->|Query| E[DynamoDB]
    D -->|Update| E
    F[GoDaddy Domain] -->|CNAME| B

Step-by-Step Process
1. Frontend Development
Design and develop the static resume website using HTML/CSS/JavaScript.
Add a visitor counter placeholder (<span id="viewer-count"></span>).
2. Host Static Website
Create an S3 bucket to host the static website.
Upload the HTML, CSS, JavaScript, and assets.
Configure the bucket as a public website or use CloudFront for secure delivery.
3. Setup CloudFront
Create a CloudFront distribution.
Point the origin to the S3 bucket.
Add an origin request policy to forward Origin headers to Lambda.
4. Custom Domain
Purchase the domain kolton.cloud via GoDaddy.
Add a CNAME record in GoDaddy to point to the CloudFront distribution.
5. Visitor Counter Backend
DynamoDB:

Create a table named cloud-resume-test with id as the partition key.
Prepopulate the table with an item: { "id": "0", "views": 0 }.
Lambda Function:

Write a Python script to:
Retrieve the visitor count from DynamoDB.
Increment the count and update it in DynamoDB.
Return the updated count as a JSON response.
Add Access-Control-Allow-Origin headers for CORS.
Test the Lambda:

Deploy the function and test its API via the Lambda console.
6. Integrate Backend with Frontend
Modify index.js to fetch visitor count from the Lambda API and display it:

const apiEndpoint = 'https://your-lambda-url.amazonaws.com/';
fetch(apiEndpoint)
  .then(response => response.json())
  .then(data => {
    document.getElementById('viewer-count').textContent = data.views;
  })
  .catch(error => console.error('Error:', error));

Upload index.js and other files to the S3 bucket.

7. Enable HTTPS
Request an SSL certificate for kolton.cloud via ACM.
Attach the certificate to the CloudFront distribution.
8. Testing
Verify the website is accessible via https://www.kolton.cloud.
Ensure the visitor counter updates correctly.
9. Optimize and Deploy
Invalidate CloudFront cache after updates.
Use tools like curl or browser DevTools to debug and verify.
Challenges Faced
CORS Errors:

Resolved by dynamically setting Access-Control-Allow-Origin in the Lambda function.
Configured CloudFront to forward Origin headers.
Region Mismatch:

Ensured Lambda and DynamoDB operated in the same region.
Cache Invalidation:

Used AWS CLI to invalidate CloudFront cache after deploying changes.
Custom Domain Integration:

Configured CNAME records in GoDaddy to point to CloudFront.
How to Run Locally
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/cloud-resume
cd cloud-resume
Open index.html in a browser to view the resume.
Future Enhancements
Add more dynamic features (e.g., blog posts or projects).
Deploy using Infrastructure as Code (e.g., AWS CloudFormation or Terraform).
Enable analytics to track visitor behavior.
License
This project is licensed under the MIT License. See the LICENSE file for details.
