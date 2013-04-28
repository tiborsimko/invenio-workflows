## This file is part of Invenio.
## Copyright (C) 2012 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from invenio.bibworkflow.tasks.my_tasks import simple_task, sleep_task, \
    save_workflow
from invenio.bibworkflow_workflow_definition import WorkflowDefinition


class workflow2(WorkflowDefinition):
    def __init__(self):
        super(workflow2, self).__init__()
        self.definition = [simple_task(5),
                           sleep_task(10),
                           simple_task(3),
                           save_workflow(),
                           simple_task(3),
                           simple_task(10)]
