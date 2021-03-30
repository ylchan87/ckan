# encoding: utf-8

'''
Helper functions to be used in the auth check functions
'''

import ckan.logic as logic
import ckan.authz as authz
from ckan.types import Context, AuthResult
from ckan import model


def _get_object(context, data_dict, name, class_name):
    # return the named item if in the context, or get it from model.class_name
    try:
        return context[name]
    except KeyError:
        model = context['model']
        if not data_dict:
            data_dict = {}
        id = data_dict.get('id', None)
        if not id:
            raise logic.ValidationError('Missing id, can not get {0} object'
                                        .format(class_name))
        obj = getattr(model, class_name).get(id)
        if not obj:
            raise logic.NotFound
        # Save in case we need this again during the request
        context[name] = obj
        return obj


def get_package_object(context: Context, data_dict=None) -> model.Package:
    return _get_object(context, data_dict, 'package', 'Package')


def get_resource_object(context: Context, data_dict=None) -> model.Resource:
    return _get_object(context, data_dict, 'resource', 'Resource')


def get_group_object(context: Context, data_dict=None) -> model.Group:
    return _get_object(context, data_dict, 'group', 'Group')


def get_user_object(context: Context, data_dict=None) -> model.User:
    return _get_object(context, data_dict, 'user_obj', 'User')


def get_activity_object(context: Context, data_dict=None) -> model.Activity:
    return _get_object(context, data_dict, 'activity', 'Activity')


def restrict_anon(context: Context) -> AuthResult:
    if authz.auth_is_anon_user(context):
        return {'success': False}
    else:
        return {'success': True}
