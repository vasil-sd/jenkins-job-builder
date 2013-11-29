# Copyright 2012 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import setuptools

from jenkins_jobs.openstack.common import setup
from jenkins_jobs.version import version_info as version

requires = setup.parse_requirements()
test_requires = setup.parse_requirements(['tools/test-requires'])
depend_links = setup.parse_dependency_links()


setuptools.setup(
    name='jenkins-job-builder',
    version=version.canonical_version_string(always=True),
    author='Hewlett-Packard Development Company, L.P.',
    author_email='openstack@lists.launchpad.net',
    description='Manage Jenkins jobs with YAML',
    license='Apache License, Version 2.0',
    url='https://github.com/openstack-ci/jenkins-job-builder',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=setup.get_cmdclass(),
    install_requires=requires,
    dependency_links=depend_links,
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    entry_points={
        'console_scripts': [
            'jenkins-jobs=jenkins_jobs.cmd:main',
        ],
        'jenkins_jobs.projects': [
            'flow=jenkins_jobs.modules.project_flow:Flow',
            'freestyle=jenkins_jobs.modules.project_freestyle:Freestyle',
            'matrix=jenkins_jobs.modules.project_matrix:Matrix',
            'maven=jenkins_jobs.modules.project_maven:Maven',
            'multijob=jenkins_jobs.modules.project_multijob:MultiJob',
        ],
        'jenkins_jobs.builders': [
            'ant=jenkins_jobs.modules.builders:ant',
            ('artifact-resolver=jenkins_jobs.modules.builders:'
             'artifact_resolver'),
            'batch=jenkins_jobs.modules.builders:batch',
            'builders-from=jenkins_jobs.modules.builders:builders_from',
            'conditional-step=jenkins_jobs.modules.builders:conditional_step',
            'copyartifact=jenkins_jobs.modules.builders:copyartifact',
            'gradle=jenkins_jobs.modules.builders:gradle',
            'grails=jenkins_jobs.modules.builders:grails',
            'inject=jenkins_jobs.modules.builders:inject',
            'maven-target=jenkins_jobs.modules.builders:maven_target',
            'msbuild=jenkins_jobs.modules.builders:msbuild',
            'multijob=jenkins_jobs.modules.builders:multijob',
            'sbt=jenkins_jobs.modules.builders:sbt',
            'shell=jenkins_jobs.modules.builders:shell',
            'trigger-builds=jenkins_jobs.modules.builders:trigger_builds',
        ],
        'jenkins_jobs.reporters': [
            'email=jenkins_jobs.modules.reporters:email',
        ],
        'jenkins_jobs.properties': [
            ('authenticated-build=jenkins_jobs.modules.properties:'
             'authenticated_build'),
            'authorization=jenkins_jobs.modules.properties:authorization',
            'build-blocker=jenkins_jobs.modules.properties:build_blocker',
            'extended-choice=jenkins_jobs.modules.properties:extended_choice',
            'github=jenkins_jobs.modules.properties:github',
            'inject=jenkins_jobs.modules.properties:inject',
            'ownership=jenkins_jobs.modules.properties:ownership',
            'priority-sorter=jenkins_jobs.modules.properties:priority_sorter',
            'promoted-build=jenkins_jobs.modules.properties:promoted_build',
            'throttle=jenkins_jobs.modules.properties:throttle',
        ],
        'jenkins_jobs.parameters': [
            'bool=jenkins_jobs.modules.parameters:bool_param',
            'choice=jenkins_jobs.modules.parameters:choice_param',
            ('dynamic-choice=jenkins_jobs.modules.parameters:'
             'dynamic_choice_param'),
            ('dynamic-choice-scriptler=jenkins_jobs.modules.parameters:'
             'dynamic_choice_scriptler_param'),
            ('dynamic-string=jenkins_jobs.modules.parameters:'
             'dynamic_string_param'),
            ('dynamic-string-scriptler=jenkins_jobs.modules.parameters:'
             'dynamic_string_scriptler_param'),
            'file=jenkins_jobs.modules.parameters:file_param',
            'label=jenkins_jobs.modules.parameters:label_param',
            'password=jenkins_jobs.modules.parameters:password_param',
            'string=jenkins_jobs.modules.parameters:string_param',
            'svn-tags=jenkins_jobs.modules.parameters:svn_tags_param',
            'text=jenkins_jobs.modules.parameters:text_param',
            ('validating-string=jenkins_jobs.modules.parameters:'
             'validating_string_param'),
        ],
        'jenkins_jobs.metadata': [
            'date=jenkins_jobs.modules.metadata:date_metadata',
            'number=jenkins_jobs.modules.metadata:number_metadata',
            'string=jenkins_jobs.modules.metadata:string_metadata',
        ],
        'jenkins_jobs.notifications': [
            'http=jenkins_jobs.modules.notifications:http_endpoint',
        ],
        'jenkins_jobs.publishers': [
            'aggregate-tests=jenkins_jobs.modules.publishers:aggregate_tests',
            'archive=jenkins_jobs.modules.publishers:archive',
            'blame-upstream=jenkins_jobs.modules.publishers:blame_upstream',
            'build-publisher=jenkins_jobs.modules.publishers:build_publisher',
            'checkstyle=jenkins_jobs.modules.publishers:checkstyle',
            'cifs=jenkins_jobs.modules.publishers:cifs',
            'claim-build=jenkins_jobs.modules.publishers:claim_build',
            'cobertura=jenkins_jobs.modules.publishers:cobertura',
            'copy-to-master=jenkins_jobs.modules.publishers:copy_to_master',
            'coverage=jenkins_jobs.modules.publishers:coverage',
            'cppcheck=jenkins_jobs.modules.publishers:cppcheck',
            'email=jenkins_jobs.modules.publishers:email',
            'email-ext=jenkins_jobs.modules.publishers:email_ext',
            ('emotional-jenkins=jenkins_jobs.modules.publishers:'
             'emotional_jenkins'),
            'fingerprint=jenkins_jobs.modules.publishers:fingerprint',
            'ftp=jenkins_jobs.modules.publishers:ftp',
            'git=jenkins_jobs.modules.publishers:git',
            ('groovy-postbuild=jenkins_jobs.modules.publishers:'
             'groovy_postbuild'),
            'html-publisher=jenkins_jobs.modules.publishers:html_publisher',
            'ircbot=jenkins_jobs.modules.publishers:ircbot',
            'jabber=jenkins_jobs.modules.publishers:jabber',
            'jacoco=jenkins_jobs.modules.publishers:jacoco',
            'jira=jenkins_jobs.modules.publishers:jira',
            'join-trigger=jenkins_jobs.modules.publishers:join_trigger',
            'junit=jenkins_jobs.modules.publishers:junit',
            'logparser=jenkins_jobs.modules.publishers:logparser',
            'maven-deploy=jenkins_jobs.modules.publishers:maven_deploy',
            'performance=jenkins_jobs.modules.publishers:performance',
            'pipeline=jenkins_jobs.modules.publishers:pipeline',
            'plot=jenkins_jobs.modules.publishers:plot',
            'post-tasks=jenkins_jobs.modules.publishers:post_tasks',
            'robot=jenkins_jobs.modules.publishers:robot',
            'scp=jenkins_jobs.modules.publishers:scp',
            'sloccount=jenkins_jobs.modules.publishers:sloccount',
            'sonar=jenkins_jobs.modules.publishers:sonar',
            'ssh=jenkins_jobs.modules.publishers:ssh',
            'stash=jenkins_jobs.modules.publishers:stash',
            'tap=jenkins_jobs.modules.publishers:tap',
            'text-finder=jenkins_jobs.modules.publishers:text_finder',
            'trigger=jenkins_jobs.modules.publishers:trigger',
            ('trigger-parameterized-builds='
             'jenkins_jobs.modules.publishers:trigger_parameterized_builds'),
            'violations=jenkins_jobs.modules.publishers:violations',
            'warnings=jenkins_jobs.modules.publishers:warnings',
            ('workspace-cleanup=jenkins_jobs.modules.publishers:'
             'workspace_cleanup'),
            'xml-summary=jenkins_jobs.modules.publishers:xml_summary',
            'xunit=jenkins_jobs.modules.publishers:xunit',
        ],
        'jenkins_jobs.scm': [
            'git=jenkins_jobs.modules.scm:git',
            'repo=jenkins_jobs.modules.scm:repo',
            'svn=jenkins_jobs.modules.scm:svn',
            'tfs=jenkins_jobs.modules.scm:tfs',
        ],
        'jenkins_jobs.triggers': [
            'build-result=jenkins_jobs.modules.triggers:build_result',
            'gerrit=jenkins_jobs.modules.triggers:gerrit',
            'github=jenkins_jobs.modules.triggers:github',
            ('github-pull-request=jenkins_jobs.modules.triggers:'
             'github_pull_request'),
            'pollscm=jenkins_jobs.modules.triggers:pollscm',
            'timed=jenkins_jobs.modules.triggers:timed',
        ],
        'jenkins_jobs.wrappers': [
            'ansicolor=jenkins_jobs.modules.wrappers:ansicolor',
            'build-name=jenkins_jobs.modules.wrappers:build_name',
            'build-user-vars=jenkins_jobs.modules.wrappers:build_user_vars',
            'copy-to-slave=jenkins_jobs.modules.wrappers:copy_to_slave',
            'env-file=jenkins_jobs.modules.wrappers:env_file',
            'inject=jenkins_jobs.modules.wrappers:inject',
            'inject-passwords=jenkins_jobs.modules.wrappers:inject_passwords',
            'jclouds=jenkins_jobs.modules.wrappers:jclouds',
            'locks=jenkins_jobs.modules.wrappers:locks',
            'mask-passwords=jenkins_jobs.modules.wrappers:mask_passwords',
            'pathignore=jenkins_jobs.modules.wrappers:pathignore',
            'port-allocator=jenkins_jobs.modules.wrappers:port_allocator',
            ('pre-scm-buildstep='
             'jenkins_jobs.modules.wrappers:pre_scm_buildstep'),
            'release=jenkins_jobs.modules.wrappers:release',
            'rvm-env=jenkins_jobs.modules.wrappers:rvm_env',
            'sauce-ondemand=jenkins_jobs.modules.wrappers:sauce_ondemand',
            'timeout=jenkins_jobs.modules.wrappers:timeout',
            'timestamps=jenkins_jobs.modules.wrappers:timestamps',
            'logfilesize = jenkins_jobs.modules.wrappers:logfilesize',
            ('workspace-cleanup=jenkins_jobs.modules.wrappers:'
             'workspace_cleanup'),
        ],
        'jenkins_jobs.modules': [
            'builders=jenkins_jobs.modules.builders:Builders',
            'general=jenkins_jobs.modules.general:General',
            'hipchat=jenkins_jobs.modules.hipchat_notif:HipChat',
            'metadata=jenkins_jobs.modules.metadata:Metadata',
            'notifications=jenkins_jobs.modules.notifications:Notifications',
            'parameters=jenkins_jobs.modules.parameters:Parameters',
            'publishers=jenkins_jobs.modules.publishers:Publishers',
            'properties=jenkins_jobs.modules.properties:Properties',
            'redmine = jenkins_jobs.modules.redmine:Redmine',
            'reporters=jenkins_jobs.modules.reporters:Reporters',
            'scm=jenkins_jobs.modules.scm:SCM',
            'triggers=jenkins_jobs.modules.triggers:Triggers',
            'wrappers=jenkins_jobs.modules.wrappers:Wrappers',
            'zuul=jenkins_jobs.modules.zuul:Zuul',
        ]
    }
)
