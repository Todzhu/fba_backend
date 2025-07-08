from fastapi import APIRouter, Depends, Body
from backend.app.biocloud.schema.analysis_tool import AnalysisToolListRequest
from backend.app.biocloud.service.analysis_tool import list_analysis_tools
from backend.database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/biocloud/analysis_tool", tags=["分析工具"])

@router.post("/list")
async def analysis_tool_list(
    req: AnalysisToolListRequest,
    db: AsyncSession = Depends(get_db)
):
    return await list_analysis_tools(
        db=db,
        page=req.page,
        page_size=req.page_size,
        category=req.category,
        func_type=req.func_type,
        search=req.search
    ) 