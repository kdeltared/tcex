# -*- coding: utf-8 -*-
"""ThreatConnect Workflow Template"""
from .common_case_management import CommonCaseManagement
from .common_case_management_collection import CommonCaseManagementCollection
from .tql import TQL

api_endpoint = '/v3/workflowTemplates'


class WorkflowTemplates(CommonCaseManagementCollection):
    def __init__(self, tcex, initial_response=None, tql_filters=None):
        super().__init__(
            tcex, api_endpoint, initial_response=initial_response, tql_filters=tql_filters
        )

    def __iter__(self):
        return self.iterate(initial_response=self.initial_response)

    def organization_id_filter(self, operator, organization_id):
        """
            The summary of the artifact
        """
        self.tql.add_filter('organizationid', operator, organization_id, TQL.Type.INTEGER)

    def assigned_user_id_filter(self, operator, assigned_user_id):
        """
            The summary of the artifact
        """
        self.tql.add_filter('assigneduserid', operator, assigned_user_id, TQL.Type.INTEGER)

    def target_id_filter(self, operator, target_id):
        """
            The summary of the artifact
        """
        self.tql.add_filter('targetid', operator, target_id, TQL.Type.INTEGER)

    def target_type_filter(self, operator, target_type):
        """
            The summary of the artifact
        """
        self.tql.add_filter('targettype', operator, target_type)

    def config_artifact_filter(self, operator, config_artifact):
        """
            The summary of the artifact
        """
        self.tql.add_filter('configartifact', operator, config_artifact)

    def name_filter(self, operator, name):
        """
            The summary of the artifact
        """
        self.tql.add_filter('name', operator, name)

    def description_filter(self, operator, description):
        """
            The summary of the artifact
        """
        self.tql.add_filter('description', operator, description)

    def config_task_filter(self, operator, config_task):
        """
            The summary of the artifact
        """
        self.tql.add_filter('configtask', operator, config_task)

    def active_filter(self, operator, active):
        """
            The summary of the artifact
        """
        self.tql.add_filter('active', operator, active)

    def id_filter(self, operator, id):
        """
            The summary of the artifact
        """
        self.tql.add_filter('id', operator, id, TQL.Type.INTEGER)

    def config_playbook_filter(self, operator, config_playbook):
        """
            The summary of the artifact
        """
        self.tql.add_filter('configplaybook', operator, config_playbook)

    def version_filter(self, operator, version):
        """
            The summary of the artifact
        """
        self.tql.add_filter('version', operator, version)

    def entity_map(self, entity):
        return WorkflowTemplate(self.tcex, **entity)


class WorkflowTemplate(CommonCaseManagement):
    def __init__(self, tcex, **kwargs):
        super().__init__(tcex, api_endpoint, kwargs)
        self._name = kwargs.get('name', None)
        self._description = kwargs.get('description', None)
        self._active = kwargs.get('active', True)
        self._version = kwargs.get('version', None)

    @property
    def required_properties(self):
        return ['name', 'description', 'active', 'version']

    @property
    def available_fields(self):
        return ['assignees', 'cases', 'organizations', 'user']

    def entity_mapper(self, entity):
        """
         Maps a dict to a Workflow Template then updates self.

         Args:
             entity (dict): The dict to map self too.
         """
        new_case = WorkflowTemplate(self.tcex, **entity)
        self.__dict__.update(new_case.__dict__)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, active):
        self._active = active

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version