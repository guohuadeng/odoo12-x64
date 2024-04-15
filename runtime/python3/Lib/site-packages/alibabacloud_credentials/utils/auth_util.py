import os

client_type = os.environ.get('ALIBABA_CLOUD_PROFILE', 'default')
environment_access_key_id = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID')
environment_access_key_secret = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET')
environment_ECSMeta_data = os.environ.get('ALIBABA_CLOUD_ECS_METADATA')
environment_credentials_file = os.environ.get('ALIBABA_CLOUD_CREDENTIALS_FILE')
private_key = None


def get_private_key(file_path):
    with open(file_path, encoding='utf-8') as f:
        key = f.read()
    return key
