variable "bucket_name" {
  description = "The name of the S3 bucket"
  type        = string
}

variable "tags" {
  description = "Tags for the S3 bucket"
  type        = map(string)
}

resource "aws_s3_bucket" "angular_app_bucket" {
  bucket = var.bucket_name

  website {
    index_document = "index.html"
    error_document = "index.html"
  }

 
    tags = var.tags
}
