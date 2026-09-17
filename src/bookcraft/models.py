from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Figure:
    id: str
    src: str
    caption: str = ""
    alt: str = ""
    full_page: bool = False


@dataclass
class Section:
    id: str
    title: str
    paragraphs: List[str] = field(default_factory=list)
    figures: List[Figure] = field(default_factory=list)


@dataclass
class Chapter:
    id: str
    title: str
    subtitle: str = ""
    sections: List[Section] = field(default_factory=list)
    start_on_recto: bool = True


@dataclass
class Book:
    title: str
    subtitle: str = ""
    author: str = ""
    editor: str = ""
    language: str = "zh-CN"
    trim_size: str = "A5"
    chapters: List[Chapter] = field(default_factory=list)
    front_matter: List[Section] = field(default_factory=list)
    appendices: List[Chapter] = field(default_factory=list)
    source_sha256: Optional[str] = None

    def chapter_ids(self) -> List[str]:
        return [chapter.id for chapter in self.chapters]

    def validate(self) -> None:
        ids = self.chapter_ids()
        if len(ids) != len(set(ids)):
            raise ValueError("chapter ids must be unique")
        if not self.title.strip():
            raise ValueError("book title is required")
