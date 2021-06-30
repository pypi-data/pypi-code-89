import io
import logging
import os
from datetime import datetime

import grpc
import requests

from . import CredCommon_pb2, MFTApi_pb2, MFTApi_pb2_grpc
from .base import ProvidesDownloadUrl, UserStorageProvider

logger = logging.getLogger(__name__)


class MFTUserStorageProvider(UserStorageProvider, ProvidesDownloadUrl):

    def __init__(self, authz_token, resource_id, context=None, resource_token=None, mft_api_endpoint=None, mft_api_secure=False, resource_per_gateway=False, **kwargs):
        super().__init__(authz_token, resource_id, context=context, **kwargs)
        self.resource_token = resource_token
        self.mft_api_endpoint = mft_api_endpoint
        self.mft_api_secure = mft_api_secure
        self.resource_per_gateway = resource_per_gateway

    def exists(self, resource_path):
        with grpc.insecure_channel(self.mft_api_endpoint) as channel:
            child_path = self._get_child_path(resource_path)
            # TODO: is this still needed?
            # parent_path, child_path = os.path.split(f"/tmp/{resource_path}".rstrip("/"))
            # get metadata for the parent path
            if child_path is not None:
                parent_path, child_path = os.path.split(child_path)
            else:
                parent_path = None
            stub = MFTApi_pb2_grpc.MFTApiServiceStub(channel)
            # Get metadata for parent directory and see if child_path exists
            request = MFTApi_pb2.FetchResourceMetadataRequest(
                # resourceId="remote-ssh-dir-resource",
                resourceId=self.resource_id,
                resourceType="SCP",
                # resourceToken="local-ssh-cred",
                resourceToken=self.resource_token,
                resourceBackend="FILE",
                resourceCredentialBackend="FILE",
                targetAgentId="agent0",
                childPath=parent_path,
                mftAuthorizationToken=self.auth_token,
            )
            try:
                response = stub.getDirectoryResourceMetadata(request)
            except Exception:
                # Could not find the parent path, so apparently doesn't exist
                logger.warning(f"Could not get metadata for {parent_path} on {self.resource_id}")
                return False
            # if not child_path, then return True since the response was
            # successful and we just need to confirm the existence of the root dir
            if child_path is None:
                return True
            return child_path in map(lambda f: f.friendlyName, list(response.directories) + list(response.files))

    def get_metadata(self, resource_path):
        with grpc.insecure_channel(self.mft_api_endpoint) as channel:
            child_path = self._get_child_path(resource_path)
            stub = MFTApi_pb2_grpc.MFTApiServiceStub(channel)
            request = MFTApi_pb2.FetchResourceMetadataRequest(
                # resourceId="remote-ssh-dir-resource",
                resourceId=self.resource_id,
                resourceType="SCP",
                # resourceToken="local-ssh-cred",
                resourceToken=self.resource_token,
                resourceBackend="FILE",
                resourceCredentialBackend="FILE",
                targetAgentId="agent0",
                childPath=child_path,
                mftAuthorizationToken=self.auth_token)
            try:
                logger.debug(f"getDirectoryResourceMetadata({request})")
                response = stub.getDirectoryResourceMetadata(request)
                logger.debug(f"getDirectoryResourceMetadata response={response}")
                directories = response.directories
                files = response.files
            except Exception:
                # if getting metadata for directory fails, try as file
                # FIXME is there a better way to determine if directory or file?
                logger.debug(f"getFileResourceMetadata({request})")
                response = stub.getFileResourceMetadata(request)
                logger.debug(f"getFileResourceMetadata response={response}")
                directories = []
                files = [response]
            directories_data = []
            for d in directories:

                dpath = os.path.join(resource_path, d.friendlyName)
                created_time = datetime.fromtimestamp(d.createdTime)
                # TODO MFT API doesn't report size
                size = 0
                directories_data.append(
                    {
                        "name": d.friendlyName,
                        # path is the relative path, or at least, relative to given resource_path
                        "path": dpath,
                        # resource_path is the id or full path to the resource
                        "resource_path": d.resourcePath,
                        "created_time": created_time,
                        "size": size,
                    }
                )
            files_data = []
            for f in files:
                user_rel_path = os.path.join(resource_path, f.friendlyName)
                # TODO do we need to check for broken symlinks?
                created_time = datetime.fromtimestamp(f.createdTime)
                size = f.resourceSize
                # full_path = datastore.path(request.user.username, user_rel_path)
                # TODO how do we register these as data products, do we need to?
                # data_product_uri = _get_data_product_uri(request, full_path)

                # data_product = request.airavata_client.getDataProduct(
                #     request.authz_token, data_product_uri)
                # mime_type = None
                # if 'mime-type' in data_product.productMetadata:
                #     mime_type = data_product.productMetadata['mime-type']
                files_data.append(
                    {
                        "name": f.friendlyName,
                        "path": user_rel_path,
                        "resource_path": f.resourcePath,
                        "created_time": created_time,
                        "size": size,
                    }
                )
            return directories_data, files_data

    def is_file(self, resource_path):
        with grpc.insecure_channel(self.mft_api_endpoint) as channel:
            child_path = self._get_child_path(resource_path)
            stub = MFTApi_pb2_grpc.MFTApiServiceStub(channel)
            # Get metadata for parent directory and see if child_path exists
            request = MFTApi_pb2.FetchResourceMetadataRequest(
                # resourceId="remote-ssh-dir-resource",
                resourceId=self.resource_id,
                resourceType="SCP",
                # resourceToken="local-ssh-cred",
                resourceToken=self.resource_token,
                resourceBackend="FILE",
                resourceCredentialBackend="FILE",
                targetAgentId="agent0",
                childPath=child_path,
                mftAuthorizationToken=self.auth_token,
            )
            try:
                stub.getFileResourceMetadata(request)
                return True
            except Exception:
                # assume that is doesn't exist, or isn't a file
                logger.warning(f"Could not get metadata for {child_path} on {self.resource_id}")
                return False

    def is_dir(self, resource_path):
        with grpc.insecure_channel(self.mft_api_endpoint) as channel:
            child_path = self._get_child_path(resource_path)
            stub = MFTApi_pb2_grpc.MFTApiServiceStub(channel)
            # Get metadata for parent directory and see if child_path exists
            request = MFTApi_pb2.FetchResourceMetadataRequest(
                # resourceId="remote-ssh-dir-resource",
                resourceId=self.resource_id,
                resourceType="SCP",
                # resourceToken="local-ssh-cred",
                resourceToken=self.resource_token,
                resourceBackend="FILE",
                resourceCredentialBackend="FILE",
                targetAgentId="agent0",
                childPath=child_path,
                mftAuthorizationToken=self.auth_token,
            )
            try:
                stub.getDirectoryResourceMetadata(request)
                return True
            except Exception:
                # assume that it doesn't exist or isn't a file
                logger.warning(f"Could not get metadata for {child_path} on {self.resource_id}")
                return False

    def get_download_url(self, resource_path):
        with grpc.insecure_channel(self.mft_api_endpoint) as channel:
            child_path = self._get_child_path(resource_path)
            stub = MFTApi_pb2_grpc.MFTApiServiceStub(channel)
            download_request = MFTApi_pb2.HttpDownloadApiRequest(
                # sourceResourceId=self.resource_id,
                # FIXME: just hacking in something to force it to work
                sourceResourceId="remote-ssh-resource",
                # sourcePath=child_path,
                sourceToken=self.resource_token,
                sourceType="SCP",
                targetAgent="agent0",
                mftAuthorizationToken=self.auth_token,
            )
            try:
                response = stub.submitHttpDownload(download_request)
                logger.debug(f"Download request for {self.resource_id}:{child_path}. Response = {response}")
                return response.url
            except Exception as e:
                logger.error(f"submitHttpDownload request {download_request} failed.")
                raise Exception(f"Failed to get download url for {resource_path}") from e

    def open(self, resource_path):
        download_url = self.get_download_url(resource_path)
        r = requests.get(download_url)
        r.raise_for_status()
        file = io.BytesIO(r.content)
        file.name = os.path.basename(resource_path)
        return file

    def _get_child_path(self, resource_path):
        """Convert possibly relative child path into absolute path."""
        if not resource_path.startswith("/"):
            # resource_path is relative, need to construct an absolute path
            if self.resource_per_gateway:
                resource_path = os.path.join(self.username, resource_path).rstrip("/")
            # If there is no child path, just return none
            if resource_path == '':
                return None
            logger.debug(f"figuring out resourcePath of {self.resource_id} ...")
            with grpc.insecure_channel(self.mft_api_endpoint) as channel:
                stub = MFTApi_pb2_grpc.MFTApiServiceStub(channel)
                request = MFTApi_pb2.FetchResourceMetadataRequest(
                    # resourceId="remote-ssh-dir-resource",
                    resourceId=self.resource_id,
                    resourceType="SCP",
                    # resourceToken="local-ssh-cred",
                    resourceToken=self.resource_token,
                    resourceBackend="FILE",
                    resourceCredentialBackend="FILE",
                    targetAgentId="agent0",
                    mftAuthorizationToken=self.auth_token)
                response = stub.getDirectoryResourceMetadata(request)
                logger.debug(f"metadata of {self.resource_id} is {response}")
                return os.path.join(response.resourcePath, resource_path)
        else:
            # resource_path appears to be absolute path
            return resource_path

    @property
    def auth_token(self):
        """Instance of CredCommon.AuthToken wrapping user's access token."""
        return CredCommon_pb2.AuthToken(userTokenAuth=CredCommon_pb2.UserTokenAuth(token=self.access_token))
