import os


class GCloudSync:

    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):

        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        # command = f"gcloud storage cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        os.system(command)

    # def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):

    #     command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
    #     # command = f"gcloud storage cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
    #     os.system(command)

    def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):
        """
        Download a single file from GCS bucket
        """
        # Ensure destination directory exists
        os.makedirs(destination, exist_ok=True)

        # IMPORTANT: destination MUST be a directory
        command = f'gsutil cp "gs://{gcp_bucket_url}/{filename}" "{destination}/"'
        print("Executing:", command)

        os.system(command)
