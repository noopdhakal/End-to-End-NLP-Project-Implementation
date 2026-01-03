import os
from hate.components.model_pusher import ModelPusher
from hate.entity.config_entity import ModelPusherConfig

def main():
    print("=== Testing ModelPusher ONLY ===")

    config = ModelPusherConfig()

    print("Bucket Name:", config.BUCKET_NAME)
    print("Trained Model Path:", config.TRAINED_MODEL_PATH)
    print("Model Name:", config.MODEL_NAME)
    print("Model Exists:", os.path.exists(config.TRAINED_MODEL_PATH))

    # IMPORTANT CHECK
    print(config.TRAINED_MODEL_PATH)
    if not os.path.exists(config.TRAINED_MODEL_PATH):
        raise FileNotFoundError("Model file does not exist locally")

    pusher = ModelPusher(config)

    artifact = pusher.initiate_model_pusher()

    print("Upload finished successfully")
    print("Uploaded to bucket:", artifact.bucket_name)

if __name__ == "__main__":
    main()
