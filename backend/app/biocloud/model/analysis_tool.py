from __future__ import annotations
from sqlalchemy import String, Integer, Text, Boolean, DateTime, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from backend.common.model import Base
from datetime import datetime

class AnalysisTool(Base):
    """分析工具表，表名为analysis_tool"""
    __tablename__ = 'analysis_tool'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="主键ID", init=False)
    name: Mapped[str] = mapped_column(String(64), nullable=False, comment="工具名称")
    description: Mapped[str] = mapped_column(Text, nullable=True, comment="工具描述")
    icon: Mapped[str] = mapped_column(String(32), nullable=True, comment="图标名")
    icon_bg: Mapped[str] = mapped_column(String(16), nullable=True, comment="图标背景色")
    icon_color: Mapped[str] = mapped_column(String(16), nullable=True, comment="图标颜色")
    category: Mapped[str] = mapped_column(String(32), nullable=True, comment="组学分类")
    type: Mapped[str] = mapped_column(String(32), nullable=True, comment="功能分类")
    views: Mapped[int] = mapped_column(Integer, default=0, comment="浏览量")
    likes: Mapped[int] = mapped_column(Integer, default=0, comment="点赞数")
    is_favorite: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否收藏")

# MySQL建表SQL参考：
# CREATE TABLE `