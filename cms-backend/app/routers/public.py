from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.site_content import SiteContent
from app.models import resources as m

router = APIRouter(prefix="/api/public", tags=["public"])


def _section(db: Session, name: str) -> dict:
    row = db.query(SiteContent).filter(SiteContent.section == name).first()
    return row.data if row else {}


@router.get("/content")
def get_public_content(db: Session = Depends(get_db)):
    def ordered(model):
        return db.query(model).order_by(model.order_index.asc(), model.id.asc()).all()

    def dump(rows, fields):
        return [{f: getattr(r, f) for f in fields} for r in rows]

    return {
        "site_settings": _section(db, "site_settings"),
        "hero": _section(db, "hero"),
        "about": _section(db, "about"),
        "stats": dump(ordered(m.Stat), ["id", "label", "value", "suffix", "icon"]),
        "vision_mission": dump(ordered(m.VisionMissionItem), ["id", "type", "icon", "title", "body", "color"]),
        "services": dump(ordered(m.Service), ["id", "icon", "title", "desc", "points", "gradient"]),
        "milestones": dump(ordered(m.Milestone), ["id", "year", "title", "desc"]),
        "portfolio": dump(ordered(m.PortfolioItem), ["id", "title", "category", "desc", "image", "tags", "size"]),
        "process_steps": dump(ordered(m.ProcessStep), ["id", "num", "title", "icon", "desc"]),
        "team": dump(ordered(m.TeamMember), ["id", "name", "role", "img", "bio", "socials"]),
        "testimonials": dump(ordered(m.Testimonial), ["id", "quote", "name", "role", "img", "rating"]),
        "blog_posts": dump(
            [r for r in ordered(m.BlogPost) if r.published],
            ["id", "title", "slug", "category", "excerpt", "content", "image", "author", "date", "read_time"],
        ),
        "faqs": dump(ordered(m.Faq), ["id", "q", "a"]),
        "trusted_by": dump(ordered(m.TrustedByLogo), ["id", "name", "logo_url"]),
    }
