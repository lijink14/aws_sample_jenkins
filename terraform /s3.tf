resource "aws_s3_bucket" "angular_app_bucket" {
  bucket = "my-angular-app-bucket-1408"

  website {
    index_document = "index.html"
    error_document = "index.html"
  }

  tags = {
    Name = "my-angular-app-bucket"
  }
}
