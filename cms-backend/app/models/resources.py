from sqlalchemy import String, Text, Integer, JSON, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import IDMixin, OrderMixin, TimestampMixin


class Stat(Base, IDMixin, OrderMixin):
    __tablename__ = "stats"

    label: Mapped[str] = mapped_column(String(120), nullable=False)
    value: Mapped[int] = mapped_column(Integer, nullable=False)
    suffix: Mapped[str] = mapped_column(String(10), default="", nullable=False)
    icon: Mapped[str] = mapped_column(String(60), default="Award", nullable=False)


class VisionMissionItem(Base, IDMixin, OrderMixin):
    __tablename__ = "vision_mission_items"

    type: Mapped[str] = mapped_column(String(40), nullable=False)  # Vision / Mission / Values
    icon: Mapped[str] = mapped_column(String(60), default="Eye", nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    color: Mapped[str] = mapped_column(String(30), default="navy", nullable=False)


class Service(Base, IDMixin, OrderMixin):
    __tablename__ = "services"

    icon: Mapped[str] = mapped_column(String(60), default="Code2", nullable=False)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    desc: Mapped[str] = mapped_column(Text, nullable=False)
    points: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    gradient: Mapped[str] = mapped_column(String(80), default="from-navy-700 to-navy-500", nullable=False)


class Milestone(Base, IDMixin, OrderMixin):
    """WhyChooseUs timeline entries."""
    __tablename__ = "milestones"

    year: Mapped[str] = mapped_column(String(10), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    desc: Mapped[str] = mapped_column(Text, nullable=False)


class PortfolioItem(Base, IDMixin, OrderMixin):
    __tablename__ = "portfolio_items"

    title: Mapped[str] = mapped_column(String(150), nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    desc: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(500), nullable=False)
    tags: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    size: Mapped[str] = mapped_column(String(20), default="normal", nullable=False)  # normal/wide/tall


class ProcessStep(Base, IDMixin, OrderMixin):
    __tablename__ = "process_steps"

    num: Mapped[str] = mapped_column(String(10), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    icon: Mapped[str] = mapped_column(String(60), default="Search", nullable=False)
    desc: Mapped[str] = mapped_column(Text, nullable=False)


class TeamMember(Base, IDMixin, OrderMixin):
    __tablename__ = "team_members"

    name: Mapped[str] = mapped_column(String(150), nullable=False)
    role: Mapped[str] = mapped_column(String(150), nullable=False)
    img: Mapped[str] = mapped_column(String(500), nullable=False)
    bio: Mapped[str] = mapped_column(Text, default="", nullable=False)
    socials: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)


class Testimonial(Base, IDMixin, OrderMixin):
    __tablename__ = "testimonials"

    quote: Mapped[str] = mapped_column(Text, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    role: Mapped[str] = mapped_column(String(200), nullable=False)
    img: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, default=5, nullable=False)


class BlogPost(Base, IDMixin, OrderMixin, TimestampMixin):
    __tablename__ = "blog_posts"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    excerpt: Mapped[str] = mapped_column(Text, nullable=False)
    content: Mapped[str] = mapped_column(Text, default="", nullable=False)
    image: Mapped[str] = mapped_column(String(500), nullable=False)
    author: Mapped[str] = mapped_column(String(150), default="", nullable=False)
    date: Mapped[str] = mapped_column(String(50), default="", nullable=False)
    read_time: Mapped[str] = mapped_column(String(20), default="5 min", nullable=False)
    published: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class Faq(Base, IDMixin, OrderMixin):
    __tablename__ = "faqs"

    q: Mapped[str] = mapped_column(String(500), nullable=False)
    a: Mapped[str] = mapped_column(Text, nullable=False)


class TrustedByLogo(Base, IDMixin, OrderMixin):
    __tablename__ = "trusted_by_logos"

    name: Mapped[str] = mapped_column(String(120), nullable=False)
    logo_url: Mapped[str] = mapped_column(String(500), default="", nullable=False)
