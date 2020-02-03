# -*- coding: utf-8 -*-
"""ThreatConnect TI Signature"""
from ..group import Group


class Signature(Group):
    """Unique API calls for Signature API Endpoints

    Valid file_types:
    + Snort
    + Suricata
    + YARA
    + ClamAV
    + OpenIOC
    + CybOX
    + Bro
    + Regex
    + SPL

    Args:
        name (str): The name for this Group.
        file_name (str): The name for the attached signature for this Group.
        file_type (str): The signature type for this Group.
        file_text (str): The signature content for this Group.
    """

    def __init__(self, tcex, name, file_name, file_type, file_text, owner=None, **kwargs):
        """Initialize Class Properties."""
        super().__init__(
            tcex, 'Signature', 'signature', 'signatures', owner=owner, name=name, **kwargs
        )
        self._data['fileName'] = file_name
        self._data['fileType'] = file_type
        self._data['fileText'] = file_text

    def download(self):
        """Download the signature.

        Returns:
            obj: The Request response of the download request.
        """
        if not self.can_update():
            self._tcex.handle_error(910, [self.type])

        return self.tc_requests.download(self.api_type, self.api_branch, self.unique_id)
