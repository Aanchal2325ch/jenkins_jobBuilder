#
# Copyright (c) 2021 The Linux Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from tests import base
import os
from jenkins_jobs.modules import project_githuborg


class TestCaseGithubOrganization(base.BaseScenariosTestCase):
    fixtures_path = os.path.join(os.path.dirname(__file__), "fixtures")
    scenarios = base.get_scenarios(fixtures_path)
    default_config_file = "/dev/null"
    klass = project_githuborg.GithubOrganization
