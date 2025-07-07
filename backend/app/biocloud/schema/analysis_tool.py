from pydantic import BaseModel, Field
from typing import Optional, List

class AnalysisToolBase(BaseModel):
    """分析工具基础"""
    name: str = Field(..., description="工具名称")
    description: Optional[str] = Field(None, description="工具描述")
    icon: Optional[str] = Field(None, description="图标名")
    icon_bg: Optional[str] = Field(None, description="图标背景色")
    icon_color: Optional[str] = Field(None, description="图标颜色")
    category: Optional[str] = Field(None, description="组学分类")
    type: Optional[str] = Field(None, description="功能分类")
    views: int = Field(0, description="浏览量")
    likes: int = Field(0, description="点赞数")
    is_favorite: bool = Field(False, description="是否收藏")

class AnalysisToolOut(AnalysisToolBase):
    """分析工具出参"""
    id: int = Field(..., description="主键ID")
    created_time: Optional[str] = Field(None, description="创建时间")
    updated_time: Optional[str] = Field(None, description="更新时间")

class AnalysisToolListRequest(BaseModel):
    """工具列表请求"""
    page: int = Field(1, description="页码")
    page_size: int = Field(8, description="每页数量")
    category: Optional[str] = Field(None, description="组学分类")
    func_type: Optional[str] = Field(None, description="功能分类")
    search: Optional[str] = Field(None, description="搜索关键字")

class AnalysisToolListResponse(BaseModel):
    """工具列表响应"""
    total: int = Field(..., description="总数")
    items: List[AnalysisToolOut] = Field(..., description="工具列表") 