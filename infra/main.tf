# Specify Terraform provider
provider "aws" {
  region = "us-west-1"  # Replace with your desired AWS region
}

# Create an S3 bucket
resource "aws_s3_bucket" "example_bucket" {
  bucket = "cloud-resume-kolton"  # Replace with your bucket name
  acl    = "private"

  tags = {
    Name        = "ExampleBucket"
    Environment = "Dev"
  }
}

# Create Lambda Function
resource "aws_lambda_function" "myfunc" {
    filename        = data.archive_file.zip.output_path
    source_code_hash = data.archive_file.zip.output_base64sha256
    function_name  = "myfunc"
    role           = aws_iam_role.iam_for_lambda.arn
    handler        = "func.handler"
    runtime        = "python3.8"
}

# Enable versioning on the bucket
resource "aws_s3_bucket_versioning" "example_bucket_versioning" {
  bucket = aws_s3_bucket.example_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Create an IAM user
resource "aws_iam_user" "example_user" {
  name = "example-user"
}

# Attach a policy to the IAM user to allow full access to the bucket
resource "aws_iam_user_policy" "example_user_policy" {
  name   = "example-user-policy"
  user   = aws_iam_user.example_user.name
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:ListBucket",
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject"
        ]
        Resource = [
          aws_s3_bucket.example_bucket.arn,
          "${aws_s3_bucket.example_bucket.arn}/*"
        ]
      }
    ]
  })
}

# Outputs for convenience
output "bucket_name" {
  value = aws_s3_bucket.example_bucket.id
}

output "iam_user_name" {
  value = aws_iam_user.example_user.name
}
