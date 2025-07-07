#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from backend.app.admin.api.router import v1 as admin_v1
from backend.app.task.api.router import v1 as task_v1
from backend.app.biocloud.api.analysis_tool import router as biocloud_analysis_tool_router

router = APIRouter()

router.include_router(admin_v1)
router.include_router(task_v1)
router.include_router(biocloud_analysis_tool_router)
