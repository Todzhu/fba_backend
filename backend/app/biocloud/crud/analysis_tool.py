from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.biocloud.model.analysis_tool import AnalysisTool
from typing import Optional, Tuple, List

async def get_analysis_tool_list(
    db: AsyncSession,
    page: int = 1,
    page_size: int = 8,
    category: Optional[str] = None,
    func_type: Optional[str] = None,
    search: Optional[str] = None
) -> Tuple[int, List[AnalysisTool]]:
    print('筛选参数 category:', repr(category), 'func_type:', repr(func_type), 'search:', repr(search))
    query = select(AnalysisTool)
    count_query = select(func.count(AnalysisTool.id))
    if category is not None and category != '':
        query = query.where(AnalysisTool.category == category)
        count_query = count_query.where(AnalysisTool.category == category)
    if func_type is not None and func_type != '':
        query = query.where(AnalysisTool.type == func_type)
        count_query = count_query.where(AnalysisTool.type == func_type)
    if search:
        query = query.where(AnalysisTool.name.ilike(f"%{search}%"))
        count_query = count_query.where(AnalysisTool.name.ilike(f"%{search}%"))
    query = query.order_by(AnalysisTool.id.desc()).offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    items = list(result.scalars().all())
    total_result = await db.execute(count_query)
    total = total_result.scalar_one()
    return total, items 