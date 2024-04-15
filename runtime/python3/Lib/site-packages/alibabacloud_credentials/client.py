from functools import wraps

from alibabacloud_credentials import credentials, providers
from alibabacloud_credentials.models import Config
from alibabacloud_credentials.utils import auth_constant as ac


def attribute_error_return_none(f):
    @wraps(f)
    def i(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except AttributeError:
            return

    return i


class Client:
    cloud_credential = None

    def __init__(self, config=None):
        if config is None:
            provider = providers.DefaultCredentialsProvider()
            self.cloud_credential = provider.get_credentials()
            return
        self.cloud_credential = self.get_credential(config)

    @staticmethod
    def get_credential(config):
        if config.type == ac.ACCESS_KEY:
            return credentials.AccessKeyCredential(config.access_key_id, config.access_key_secret)
        elif config.type == ac.STS:
            return credentials.StsCredential(config.access_key_id, config.access_key_secret, config.security_token)
        elif config.type == ac.BEARER:
            return credentials.BearerTokenCredential(config.bearer_token)
        elif config.type == ac.ECS_RAM_ROLE:
            return credentials.EcsRamRoleCredential(
                config.access_key_id,
                config.access_key_secret,
                config.security_token,
                0,
                providers.EcsRamRoleCredentialProvider(config=config)
            )
        elif config.type == ac.CREDENTIALS_URI:
            return credentials.CredentialsURICredential(config.credentials_uri)
        elif config.type == ac.RAM_ROLE_ARN:
            return credentials.RamRoleArnCredential(
                config.access_key_id,
                config.access_key_secret,
                config.security_token,
                0,
                providers.RamRoleArnCredentialProvider(config=config)
            )
        elif config.type == ac.RSA_KEY_PAIR:
            return credentials.RsaKeyPairCredential(
                config.access_key_id,
                config.access_key_secret,
                0,
                providers.RsaKeyPairCredentialProvider(config=config)
            )
        return providers.DefaultCredentialsProvider().get_credentials()

    def get_access_key_id(self):
        return self.cloud_credential.get_access_key_id()

    def get_access_key_secret(self):
        return self.cloud_credential.get_access_key_secret()

    def get_security_token(self):
        return self.cloud_credential.get_security_token()

    async def get_access_key_id_async(self):
        return await self.cloud_credential.get_access_key_id_async()

    async def get_access_key_secret_async(self):
        return await self.cloud_credential.get_access_key_secret_async()

    async def get_security_token_async(self):
        return await self.cloud_credential.get_security_token_async()

    @attribute_error_return_none
    def get_type(self):
        return self.cloud_credential.credential_type

    @attribute_error_return_none
    def get_bearer_token(self):
        return self.cloud_credential.bearer_token
