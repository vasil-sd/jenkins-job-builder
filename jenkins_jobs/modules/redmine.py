# Copyright 2013 ELVEES NeoTek CJSC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Allows to connect Jenkins job to Redmine project.

Requires the Jenkins `Redmine Plugin.
<https://wiki.jenkins-ci.org/display/JENKINS/Redmine+Plugin>`_

:arg string website: Redmine website entry name 
    (as set in Redmine Plugin)
:arg string project: Redmine project name within 
    specified site

**Component**: redmine
  :Macro: redmine
  :Entry Point: jenkins_jobs.redmine

Example::

  job:
    name: test_job

    redmine:
      website: Redmine
      project: documentation
"""


import xml.etree.ElementTree as XML
import jenkins_jobs.modules.base

class Redmine(jenkins_jobs.modules.base.Base):
    sequence = 25

    def gen_xml(self, parser, xml_parent, data):
        properties = xml_parent.find('properties')
        if properties is None:
            properties = XML.SubElement(xml_parent, 'properties')

        if data.get('redmine', None) is not None:
            redmine_data = data['redmine']
            redmine_project_tag = XML.SubElement(properties,
                                                 'hudson.plugins.redmine.'
                                                 'RedmineProjectProperty')
            XML.SubElement(redmine_project_tag, 'redmineWebsiteName').text = redmine_data['website']
            XML.SubElement(redmine_project_tag, 'projectName').text = redmine_data['project']
