from providers.aws.lib.audit_info.audit_info import current_audit_info
from providers.aws.services.appstream.appstream_service import AppStream

appstream_client = AppStream(current_audit_info)
