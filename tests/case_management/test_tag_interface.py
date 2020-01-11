# -*- coding: utf-8 -*-
"""Test the TcEx Case Management Module."""
import os
from tcex.case_management.tql import TQL

from ..tcex_init import tcex
from .cm_helpers import CMHelper


class TestTag:
    """Test TcEx CM Tag Interface."""

    cm = None
    cm_helper = None
    test_obj = None
    test_obj_collection = None

    def setup_class(self):
        """Configure setup before all tests."""
        self.cm = tcex.cm
        self.test_obj = self.cm.tag()
        self.test_obj_collection = self.cm.tags()

    def setup_method(self):
        """Configure setup before all tests."""
        self.cm_helper = CMHelper(self.cm)

    def teardown_method(self):
        """Configure teardown before all tests."""
        if os.getenv('TEARDOWN_METHOD') is None:
            self.cm_helper.cleanup()

    def test_tag_filter_keywords(self):
        """Test filter keywords."""
        # print(self.test_obj._doc_string)
        # print(self.test_obj_collection._filter_map_method)
        # print(self.test_obj_collection._filter_class)
        for keyword in self.test_obj_collection.filter.keywords:
            if keyword not in self.test_obj_collection.filter.implemented_keywords:
                assert False, f'Missing TQL keyword {keyword}.'

    def test_tag_properties(self):
        """Test properties."""
        for prop_string, prop_data in self.test_obj.properties.items():
            prop_read_only = prop_data.get('read-only', False)
            prop_string = self.cm_helper.camel_to_snake(prop_string)

            # ensure class has property
            assert hasattr(
                self.test_obj, prop_string
            ), f'Missing {prop_string} property. read-only: {prop_read_only}'

    def test_tag_create(self, request):
        """Test Artifact Creation"""
        # tag data
        tag_data = {
            'description': f'a description for {request.node.name}',
            'name': request.node.name,
        }

        # create tag
        tag = self.cm.tag(**tag_data)
        tag.submit()

        # get tag from API to use in asserts
        tag = self.cm.tag(id=tag.id)
        tag.get()

        # run assertions on returned data
        assert tag.name == tag_data.get('name')
        assert tag.description == tag_data.get('description')

        # delete tag
        tag.delete()

    def test_tag_get_single(self, request):
        """Test Artifact Creation"""
        # tag data
        tag_data = {
            'description': f'a description for {request.node.name}',
            'name': request.node.name,
        }

        # create tag
        tag = self.cm.tag(**tag_data)
        tag.submit()

        # get tag from API to use in asserts
        tag = self.cm.tag(id=tag.id)
        tag.get()

        # run assertions on returned data
        assert tag.name == tag_data.get('name')
        assert tag.description == tag_data.get('description')

        # delete tag
        tag.delete()

    def test_tag_get_many(self, request):
        """Test Artifact Creation"""
        # tag data
        tag_data = {
            'description': f'a description for {request.node.name}',
            'name': request.node.name,
        }

        # create tag
        tag = self.cm.tag(**tag_data)
        tag.submit()

        # iterate over all artifact looking for needle
        for t in self.cm.tags():
            if t.name == tag_data.get('name'):
                assert t.name == tag_data.get('name')
                assert t.description == tag_data.get('description')
                break
        else:
            assert False

        # delete tag
        tag.delete()

    def test_tag_get_by_tql_filter_case_id(self, request):
        """Test Tag Get by TQL"""
        tag_data = {
            'name': request.node.name,
        }

        # create case
        case = self.cm_helper.create_case(tags=tag_data)

        # retrieve tags using TQL
        tags = self.cm.tags()
        tags.filter.case_id(TQL.Operator.EQ, case.id)

        for t in tags:
            if t.name.lower() == 'pytest':
                continue

            assert t.name == tag_data.get('name')
            break
        else:
            assert False, 'No artifact returned for TQL'

    def test_tag_get_by_tql_filter_id(self, request):
        """Test Tag Get by TQL"""
        tag_data = {
            'description': f'a description for {request.node.name}',
            'name': request.node.name,
        }

        # create tag
        tag = self.cm.tag(**tag_data)
        tag.submit()

        # retrieve tags using TQL
        tags = self.cm.tags()
        tags.filter.id(TQL.Operator.EQ, tag.id)

        for tag in tags:
            assert tag.name == tag_data.get('name')
            assert tag.description == tag_data.get('description')
            break
        else:
            assert False, 'No artifact returned for TQL'

        # delete tag
        tag.delete()

    def test_tag_get_by_tql_filter_name(self, request):
        """Test Tag Get by TQL"""
        tag_data = {
            'description': f'a description for {request.node.name}',
            'name': request.node.name,
        }

        # create tag
        tag = self.cm.tag(**tag_data)
        tag.submit()

        # retrieve tags using TQL
        tags = self.cm.tags()
        tags.filter.name(TQL.Operator.EQ, tag_data.get('name'))

        for tag in tags:
            assert tag.name == tag_data.get('name')
            assert tag.description == tag_data.get('description')
            break
        else:
            assert False, 'No artifact returned for TQL'

        # delete tag
        tag.delete()

    def test_tag_get_by_tql_filter_owner(self, request):
        """Test Tag Get by TQL"""
        tag_data = {
            'description': f'a description for {request.node.name}',
            'name': request.node.name,
        }

        # create tag
        tag = self.cm.tag(**tag_data)
        tag.submit()

        # retrieve tags using TQL
        tags = self.cm.tags()
        tags.filter.id(TQL.Operator.EQ, tag.id)
        tags.filter.owner(TQL.Operator.EQ, 2)

        for tag in tags:
            assert tag.name == tag_data.get('name')
            assert tag.description == tag_data.get('description')
            break
        else:
            assert False, 'No artifact returned for TQL'

        # delete tag
        tag.delete()

    def test_tag_get_by_tql_filter_owner_name(self, request):
        """Test Tag Get by TQL"""
        tag_data = {
            'description': f'a description for {request.node.name}',
            'name': request.node.name,
        }

        # create tag
        tag = self.cm.tag(**tag_data)
        tag.submit()

        # retrieve tags using TQL
        tags = self.cm.tags()
        tags.filter.id(TQL.Operator.EQ, tag.id)
        tags.filter.owner_name(TQL.Operator.EQ, 'TCI')

        for tag in tags:
            assert tag.name == tag_data.get('name')
            assert tag.description == tag_data.get('description')
            break
        else:
            assert False, 'No artifact returned for TQL'

        # delete tag
        tag.delete()

    def test_tag_get_by_tql_filter_tql(self, request):
        """Test Tag Get by TQL"""
        tag_data = {
            'description': f'a description for {request.node.name}',
            'name': request.node.name,
        }

        # create tag
        tag = self.cm.tag(**tag_data)
        tag.submit()

        # retrieve tags using TQL
        tags = self.cm.tags()
        tags.filter.tql(f'id EQ {tag.id}')

        for tag in tags:
            assert tag.name == tag_data.get('name')
            assert tag.description == tag_data.get('description')
            break
        else:
            assert False, 'No artifact returned for TQL'

        # delete tag
        tag.delete()
