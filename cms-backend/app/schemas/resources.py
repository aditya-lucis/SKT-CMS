from typing import Optional, Any
from pydantic import BaseModel, ConfigDict


def _out_config():
    return ConfigDict(from_attributes=True)


# ---------- Stat ----------
class StatBase(BaseModel):
    label: str
    value: int
    suffix: str = ""
    icon: str = "Award"


class StatCreate(StatBase):
    order_index: Optional[int] = None


class StatUpdate(BaseModel):
    label: Optional[str] = None
    value: Optional[int] = None
    suffix: Optional[str] = None
    icon: Optional[str] = None
    order_index: Optional[int] = None


class StatOut(StatBase):
    model_config = _out_config()
    id: int
    order_index: int


# ---------- VisionMissionItem ----------
class VisionMissionBase(BaseModel):
    type: str
    icon: str = "Eye"
    title: str
    body: str
    color: str = "navy"


class VisionMissionCreate(VisionMissionBase):
    order_index: Optional[int] = None


class VisionMissionUpdate(BaseModel):
    type: Optional[str] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    color: Optional[str] = None
    order_index: Optional[int] = None


class VisionMissionOut(VisionMissionBase):
    model_config = _out_config()
    id: int
    order_index: int


# ---------- Service ----------
class ServiceBase(BaseModel):
    icon: str = "Code2"
    title: str
    desc: str
    points: list[str] = []
    gradient: str = "from-navy-700 to-navy-500"


class ServiceCreate(ServiceBase):
    order_index: Optional[int] = None


class ServiceUpdate(BaseModel):
    icon: Optional[str] = None
    title: Optional[str] = None
    desc: Optional[str] = None
    points: Optional[list[str]] = None
    gradient: Optional[str] = None
    order_index: Optional[int] = None


class ServiceOut(ServiceBase):
    model_config = _out_config()
    id: int
    order_index: int


# ---------- Milestone ----------
class MilestoneBase(BaseModel):
    year: str
    title: str
    desc: str


class MilestoneCreate(MilestoneBase):
    order_index: Optional[int] = None


class MilestoneUpdate(BaseModel):
    year: Optional[str] = None
    title: Optional[str] = None
    desc: Optional[str] = None
    order_index: Optional[int] = None


class MilestoneOut(MilestoneBase):
    model_config = _out_config()
    id: int
    order_index: int


# ---------- PortfolioItem ----------
class PortfolioItemBase(BaseModel):
    title: str
    category: str
    desc: str
    image: str
    tags: list[str] = []
    size: str = "normal"


class PortfolioItemCreate(PortfolioItemBase):
    order_index: Optional[int] = None


class PortfolioItemUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    desc: Optional[str] = None
    image: Optional[str] = None
    tags: Optional[list[str]] = None
    size: Optional[str] = None
    order_index: Optional[int] = None


class PortfolioItemOut(PortfolioItemBase):
    model_config = _out_config()
    id: int
    order_index: int


# ---------- ProcessStep ----------
class ProcessStepBase(BaseModel):
    num: str
    title: str
    icon: str = "Search"
    desc: str


class ProcessStepCreate(ProcessStepBase):
    order_index: Optional[int] = None


class ProcessStepUpdate(BaseModel):
    num: Optional[str] = None
    title: Optional[str] = None
    icon: Optional[str] = None
    desc: Optional[str] = None
    order_index: Optional[int] = None


class ProcessStepOut(ProcessStepBase):
    model_config = _out_config()
    id: int
    order_index: int


# ---------- TeamMember ----------
class TeamMemberBase(BaseModel):
    name: str
    role: str
    img: str
    bio: str = ""
    socials: dict[str, Any] = {}


class TeamMemberCreate(TeamMemberBase):
    order_index: Optional[int] = None


class TeamMemberUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    img: Optional[str] = None
    bio: Optional[str] = None
    socials: Optional[dict[str, Any]] = None
    order_index: Optional[int] = None


class TeamMemberOut(TeamMemberBase):
    model_config = _out_config()
    id: int
    order_index: int


# ---------- Testimonial ----------
class TestimonialBase(BaseModel):
    quote: str
    name: str
    role: str
    img: str
    rating: int = 5


class TestimonialCreate(TestimonialBase):
    order_index: Optional[int] = None


class TestimonialUpdate(BaseModel):
    quote: Optional[str] = None
    name: Optional[str] = None
    role: Optional[str] = None
    img: Optional[str] = None
    rating: Optional[int] = None
    order_index: Optional[int] = None


class TestimonialOut(TestimonialBase):
    model_config = _out_config()
    id: int
    order_index: int


# ---------- BlogPost ----------
class BlogPostBase(BaseModel):
    title: str
    slug: str
    category: str
    excerpt: str
    content: str = ""
    image: str
    author: str = ""
    date: str = ""
    read_time: str = "5 min"
    published: bool = True


class BlogPostCreate(BlogPostBase):
    order_index: Optional[int] = None


class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    category: Optional[str] = None
    excerpt: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None
    author: Optional[str] = None
    date: Optional[str] = None
    read_time: Optional[str] = None
    published: Optional[bool] = None
    order_index: Optional[int] = None


class BlogPostOut(BlogPostBase):
    model_config = _out_config()
    id: int
    order_index: int


# ---------- Faq ----------
class FaqBase(BaseModel):
    q: str
    a: str


class FaqCreate(FaqBase):
    order_index: Optional[int] = None


class FaqUpdate(BaseModel):
    q: Optional[str] = None
    a: Optional[str] = None
    order_index: Optional[int] = None


class FaqOut(FaqBase):
    model_config = _out_config()
    id: int
    order_index: int


# ---------- TrustedByLogo ----------
class TrustedByLogoBase(BaseModel):
    name: str
    logo_url: str = ""


class TrustedByLogoCreate(TrustedByLogoBase):
    order_index: Optional[int] = None


class TrustedByLogoUpdate(BaseModel):
    name: Optional[str] = None
    logo_url: Optional[str] = None
    order_index: Optional[int] = None


class TrustedByLogoOut(TrustedByLogoBase):
    model_config = _out_config()
    id: int
    order_index: int
