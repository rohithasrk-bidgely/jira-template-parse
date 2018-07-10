from constants import (BACKEND_DEPLOYMENT, FRONTEND_DEPLOYMENT, SEQUENCE,
                       TYPE_OPTIONS, BUILD_VERSIONS)


class Validation(object):
    """
    Validation methods for the fields of a JIRA ticket
    """

    @staticmethod
    def validate_type(issue_type):
        if(len(issue_type)) < 1:
            raise ValueError("Type is not specified")
        elif type(issue_type) == list:
            n = 0
            for i in TYPE_OPTIONS:
                if i in issue_type: n+=1
                if n==0: raise ValueError("Invalid Type")

    @staticmethod
    def validate_frontend(frontend):
        for i in frotend:
            if not FRONTEND_DEPLOYMENT.get(i, False):
                raise ValueError("Invalid frontend technology {}".format(i))

    @staticmethod
    def validate_build_versions(build_versions):
        for i in build_versions:
            name, version = i.split(':')
            if not version.strip().startswith(BUILD_VERSIONS[name.strip()]):
                raise ValueError("Invalid version numbers")

    @staticmethod
    def validate_backend(backend):
        build_versions = backend.get('Build Versions')
        if not build_versions or len(build_versions) == 0:
            raise ValueError("Build version is a mandatory field")
        else: validate_build_versions(build_versions)
        rpms = backend.get('RPMS')
        schema_changes = backend.get('Schema Changes', False)
        if not schema_changes or len(schema_changes) == 0:
            raise ValueError("Schema Changes must be present")
        for i in rpms:
            for j in rpms[i]:
                if not BACKEND_DEPLOYMENT.get(j, False):
                    raise ValueError("Invalid backend technology {}".format(j))

    @staticmethod
    def validate_configuration(description):
        backend = description.get('Backend Deployment', False)
        if backend: validate_backend(backend)
        else: raise ValueError("Backend section not found")

    @staticmethod
    def validate_code_deployment(description):
        frontend = description.get('Front End Deployment', False)
        backend = description.get('Backend Deployment', False)
        if not frontend and not backend:
            raise ValueError("Any one of the code deployments must be present")
        if frontend: validate_frontend(frontend)
        if backend: validate_backend(backend)

    @staticmethod
    def validate_mandatory_fields(description):
        reason = description.get('Reason for change', False)
        build_version = description.get('Build Version', False)
        git_tag = description.get('Git Tag', False)
        sequence = description.get('Sequence', False)
        build_versions = description.get('Build Versions', False)
        if not reason or len(reason) == 0:
            raise ValueError("Reason is a mandatory field")

    @staticmethod
    def validate_approver_and_reviewer(description):
        approver = description.get('Approver', False)
        reviewer = description.get('Reviewer', False)
        if approver=='' or reviewer=='' or reviewer=="----":
            raise ValueError("Approver or Reviewer field not filled")

    @staticmethod
    def validate(description):
        issue_type = description.get('Type')
        validate_type(issue_type)
        if 'Configuration' in issue_type:
            validate_configuration(description)
        if 'Code deployment' in issue_type:
            validate_code_deployment(description)
        validate_mandatory_fields(description)
        Validation.validate_approver_and_reviewer(description)
        print("Validated all the fields. Good to go!")


validate_type = Validation.validate_type
validate_code_deployment = Validation.validate_code_deployment
validate_mandatory_fields = Validation.validate_mandatory_fields
validate_frontend = Validation.validate_frontend
validate_build_versions = Validation.validate_build_versions
validate_backend = Validation.validate_backend
validate_configuration = Validation.validate_configuration
