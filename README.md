# Machine Sorting

## Setup

This project is meant to run in a docker container. The dockerfile attached builds the container and the compose file assumes the docker image is called `mlworker`. The biggest thing is the environment variables - the `REDIS_URL` and `MODEL_PATH` are required while `MODEL_IMAGE_SIZE` is optional. If `MODEL_IMAGE_SIZE` is not provided it assumes a default size of 512.

Example setup on a local machine would be:

1. `docker build --no-cache -t mlworker .`
2. `docker compose up`

## Input

1. The job needs to be placed on the `sortFileQueue` in redis
2. The input needs to be json:
   ```
   {
       'id': 'pdf_file_id',
       'url': 'url_for_pdf_file'
   }
   ```

## Output

1. The worker will place the job on the `processorQueue` in redis
2. The result is json:
   ```
   {
       "id": "pdf_file_id",
       "allSorted": boolean,
       "partialSort": boolean,
       "type": 4,
       "documents": [
           {
               "className": "Some Bank",
               "pages": [1, 2, 3],
               "date": "2019-01-31",
               "amount": null
           }],
   }
   ```

## Workflow

1. Download pdf from url
2. Convert pdf to an array of images
3. Predict what class each image is
4. Attempt to get the page number for each image based on what class was predicted
5. Create document(s)
    1. For now... only pdfs with one document are sorted
    2. For now... only documents with incrementing page numbers are sorted
    3. Then the date is extracted based on the class
    4. If the class requires an amount, it also attempts to extract it

