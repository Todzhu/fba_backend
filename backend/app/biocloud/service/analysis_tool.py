from backend.app.biocloud.crud.analysis_tool import get_analysis_tool_list
from backend.app.biocloud.schema.analysis_tool import AnalysisToolListResponse, AnalysisToolOut
from backend.common.response.response_schema import response_base
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from backend.app.biocloud.model.analysis_tool import AnalysisTool
from sqlalchemy import select

async def list_analysis_tools(
    db: AsyncSession,
    page: int = 1,
    page_size: int = 8,
    category: Optional[str] = None,
    func_type: Optional[str] = None,
    search: Optional[str] = None
):
    total, items = await get_analysis_tool_list(db, page, page_size, category, func_type, search)
    data = [AnalysisToolOut(
        id=tool.id,
        name=tool.name,
        description=tool.description,
        icon=tool.icon,
        icon_bg=tool.icon_bg,
        icon_color=tool.icon_color,
        category=tool.category,
        type=tool.type,
        views=tool.views,
        likes=tool.likes,
        is_favorite=tool.is_favorite,
        created_time=str(tool.created_time) if tool.created_time else None,
        updated_time=str(tool.updated_time) if tool.updated_time else None
    ) for tool in items]
    return response_base.success(data=AnalysisToolListResponse(total=total, items=data)) 