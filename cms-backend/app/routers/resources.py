from app.crud_factory import build_crud_router
from app.models import resources as m
from app.schemas import resources as s

stats_router = build_crud_router(
    model=m.Stat, schema_out=s.StatOut, schema_create=s.StatCreate, schema_update=s.StatUpdate,
    prefix="/api/stats", tag="stats",
)

vision_mission_router = build_crud_router(
    model=m.VisionMissionItem, schema_out=s.VisionMissionOut,
    schema_create=s.VisionMissionCreate, schema_update=s.VisionMissionUpdate,
    prefix="/api/vision-mission", tag="vision-mission",
)

services_router = build_crud_router(
    model=m.Service, schema_out=s.ServiceOut, schema_create=s.ServiceCreate, schema_update=s.ServiceUpdate,
    prefix="/api/services", tag="services",
)

milestones_router = build_crud_router(
    model=m.Milestone, schema_out=s.MilestoneOut, schema_create=s.MilestoneCreate, schema_update=s.MilestoneUpdate,
    prefix="/api/milestones", tag="milestones",
)

portfolio_router = build_crud_router(
    model=m.PortfolioItem, schema_out=s.PortfolioItemOut,
    schema_create=s.PortfolioItemCreate, schema_update=s.PortfolioItemUpdate,
    prefix="/api/portfolio", tag="portfolio",
)

process_steps_router = build_crud_router(
    model=m.ProcessStep, schema_out=s.ProcessStepOut,
    schema_create=s.ProcessStepCreate, schema_update=s.ProcessStepUpdate,
    prefix="/api/process-steps", tag="process-steps",
)

team_router = build_crud_router(
    model=m.TeamMember, schema_out=s.TeamMemberOut,
    schema_create=s.TeamMemberCreate, schema_update=s.TeamMemberUpdate,
    prefix="/api/team", tag="team",
)

testimonials_router = build_crud_router(
    model=m.Testimonial, schema_out=s.TestimonialOut,
    schema_create=s.TestimonialCreate, schema_update=s.TestimonialUpdate,
    prefix="/api/testimonials", tag="testimonials",
)

blog_router = build_crud_router(
    model=m.BlogPost, schema_out=s.BlogPostOut, schema_create=s.BlogPostCreate, schema_update=s.BlogPostUpdate,
    prefix="/api/blog", tag="blog",
)

faqs_router = build_crud_router(
    model=m.Faq, schema_out=s.FaqOut, schema_create=s.FaqCreate, schema_update=s.FaqUpdate,
    prefix="/api/faqs", tag="faqs",
)

trusted_by_router = build_crud_router(
    model=m.TrustedByLogo, schema_out=s.TrustedByLogoOut,
    schema_create=s.TrustedByLogoCreate, schema_update=s.TrustedByLogoUpdate,
    prefix="/api/trusted-by", tag="trusted-by",
)

all_resource_routers = [
    stats_router,
    vision_mission_router,
    services_router,
    milestones_router,
    portfolio_router,
    process_steps_router,
    team_router,
    testimonials_router,
    blog_router,
    faqs_router,
    trusted_by_router,
]
