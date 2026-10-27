#!/usr/bin/env python3

import aws_cdk as cdk

from hr_leave_portal_new.hr_leave_portal_new_stack import HrLeavePortalNewStack


app = cdk.App()
HrLeavePortalNewStack(app, "HrLeavePortalNewStack")

app.synth()
