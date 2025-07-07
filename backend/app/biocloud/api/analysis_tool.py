from fastapi import APIRouter, Depends, Body
from backend.app.biocloud.schema.analysis_tool import AnalysisToolListRequest
from backend.app.biocloud.service.analysis_tool import list_analysis_tools, toggle_favorite
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

@router.post("/favorite")
async def analysis_tool_favorite(
    tool_id: int = Body(..., embed=True),
    is_favorite: bool = Body(..., embed=True),
    db: AsyncSession = Depends(get_db)
):
    return await toggle_favorite(db, tool_id, is_favorite) 