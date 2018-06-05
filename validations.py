from constants import TYPE_OPTIONS


class Validation(object):
    def validate_type(self, issue_type):
        if(len(issue_type)) < 1:
            raise ValueError("Type is not specified")
        elif type(issue_type) == list:
            n = 0
            for i in TYPE_OPTIONS:
                if i in issue_type: n+=1
                if n==0: raise ValueError("Invalid Type")

    def validate_configuration(self, description):
        schema_changes = description.get('Schema Changes', False)
        if not schema_changes:
            schema_changes = description.get('Config Changes', False)
        if not schema_changes or len(schema_changes) == 0: 
            raise ValueError("Schema Changes must be present")

    def validate_frontend(self, frontend):
        pass

    def validate_backend(self, backend):
        pass

    def validate_code_deployment(self, description):
        frontend = description.get('Front End Deployment', False)
        backend = description.get('Backend Deployment', False)
        if not frontend and not backend:
            raise ValueError("Any one of the code deployments must be present")
        if frontend: validate_frontend(frontend)
        if backend: validate_backend(backend)

    def validate_mandatory_fields(self, description):
        reason = description.get('Reason for change', False)
        build_version = description.get('Build Version', False)
        git_tag = description.get('Git Tag', False)
        sequence = description.get('Sequence', False)
        build_versions = description.get('Build Versions', False)
        if not reason or len(reason) == 0:
            raise ValueError("Reason is a mandatory field")
        if not build_version or len(build_version) == 0:
            raise ValueError("Build version is a mandatory field")
        if not git_tag or len(git_tag) == 0:
            raise ValueError("Git tag is a mandatory field")
        if not sequence or len(sequence) == 0:
            raise ValueError("Sequence is a mandatory field")
        if not build_versions or len(build_versions) == 0:
            raise ValueError("Build version is a mandatory field")

    def validate(self, f, description):
        issue_type = description.get('Type')
        self.validate_type(issue_type)
        if 'Configuration' in issue_type:
            self.validate_configuration(description)
        if 'Code deployment' in issue_type:
            self.validate_code_deployment(description)
        self.validate_mandatory_fields(description)
        print("Validated all the fields. Good to go!")
