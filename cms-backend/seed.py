"""
Seeds the database with the content that currently lives in
company-profile/src/data/content.js, so the CMS opens pre-filled with
everything already on the live site instead of empty tables.

Run once after the tables exist:
    ./venv/bin/python seed.py
Safe to re-run: it clears each table before reinserting (idempotent).
"""
from app.core.database import SessionLocal, engine, Base
from app.models.site_content import SiteContent
from app.models import resources as m
import app.models  # noqa: F401 ensure metadata is fully populated

Base.metadata.create_all(bind=engine)

db = SessionLocal()


def img(photo_id: str, w: int = 1200, q: int = 80) -> str:
    return f"https://images.unsplash.com/photo-{photo_id}?auto=format&fit=crop&w={w}&q={q}"


def upsert_section(section: str, data: dict):
    row = db.query(SiteContent).filter(SiteContent.section == section).first()
    if row:
        row.data = data
    else:
        db.add(SiteContent(section=section, data=data))


# ---------------------------------------------------------------- SECTIONS
upsert_section("site_settings", {
    "company_name": "SKT",
    "tagline": "Building The Future Through Innovation & Technology",
    "email": "hello@nexustech.io",
    "phone": "+1 (415) 555-0199",
    "address": "One Market Street, Suite 1500, San Francisco, CA 94105",
    "social": [
        {"name": "LinkedIn", "icon": "Linkedin", "href": "#"},
        {"name": "Twitter", "icon": "Twitter", "href": "#"},
        {"name": "GitHub", "icon": "Github", "href": "#"},
        {"name": "Instagram", "icon": "Instagram", "href": "#"},
        {"name": "YouTube", "icon": "Youtube", "href": "#"},
    ],
    "meta_title": "SKT CMS — Software, ERP, HIS, Cloud & AI Solutions",
    "meta_description": "SKT builds custom software, ERP, hospital information systems, cloud, and AI solutions for ambitious companies worldwide.",
})

upsert_section("hero", {
    "badge": "Trusted by 180+ global clients",
    "headline_1": "Building The Future",
    "headline_2": "Through Innovation",
    "headline_highlight": "& Technology",
    "subheadline": "We design, engineer, and scale software that moves businesses forward — from custom platforms to enterprise AI.",
    "cta_primary_label": "Start a Project",
    "cta_primary_href": "#contact",
    "cta_secondary_label": "View Our Work",
    "cta_secondary_href": "#portfolio",
    "background_image": img("1451187580459-43490279c0fa", 1920),
})

upsert_section("about", {
    "eyebrow": "About SKT",
    "title": "We engineer software that",
    "highlight_word": "moves the needle",
    "subtitle": "Since 2013, SKT has partnered with ambitious companies to design, build, and scale the software that runs their business.",
    "office_image": img("1497366216548-37526070297c", 1200),
    "highlights": [
        "Senior-only engineering pods",
        "Fixed delivery dates, no surprises",
        "SOC 2 Type II & ISO 27001",
        "24/7 SRE coverage post-launch",
    ],
    "badge_text": "12+ Years of Excellence",
})

# ---------------------------------------------------------------- LISTS

def reset(model):
    db.query(model).delete()


reset(m.Stat)
for i, s in enumerate([
    {"value": 320, "suffix": "+", "label": "Projects Delivered", "icon": "Briefcase"},
    {"value": 180, "suffix": "+", "label": "Global Clients", "icon": "Users"},
    {"value": 95, "suffix": "", "label": "Expert Developers", "icon": "Code2"},
    {"value": 24, "suffix": "", "label": "Countries Served", "icon": "Globe"},
    {"value": 12, "suffix": "+", "label": "Years of Experience", "icon": "Award"},
]):
    db.add(m.Stat(order_index=i, **s))

reset(m.VisionMissionItem)
for i, v in enumerate([
    {"type": "Vision", "icon": "Eye", "color": "navy",
     "title": "To be the most trusted technology partner for visionary enterprises",
     "body": "We envision a world where every organization — from bold startups to Fortune 500s — has access to world-class engineering, design, and AI capabilities that compound their impact on the world."},
    {"type": "Mission", "icon": "Target", "color": "emerald",
     "title": "Engineer software that moves businesses forward — measurably",
     "body": "Our mission is to translate ambitious business goals into resilient, scalable, and delightful software. We obsess over outcomes, ship relentlessly, and partner with our clients for the long haul."},
    {"type": "Values", "icon": "Heart", "color": "cyan",
     "title": "Craft, candor, and curiosity in everything we ship",
     "body": "We hold ourselves to a higher bar. We choose craft over convenience, candor over comfort, and curiosity over complacency. These principles shape every line of code and every client conversation."},
]):
    db.add(m.VisionMissionItem(order_index=i, **v))

reset(m.Service)
for i, sv in enumerate([
    {"icon": "Code2", "title": "Software Development", "gradient": "from-navy-700 to-navy-500",
     "desc": "Custom software engineered for scale — from MVPs to enterprise platforms handling millions of transactions daily.",
     "points": ["Architecture review", "Distributed systems", "Performance audits"]},
    {"icon": "Database", "title": "ERP System", "gradient": "from-emerald-brand-600 to-emerald-brand-400",
     "desc": "Unified ERP platforms that connect finance, HR, supply chain, and operations into a single source of truth.",
     "points": ["SAP / Oracle migration", "Custom modules", "Workflow automation"]},
    {"icon": "Stethoscope", "title": "Hospital Information System", "gradient": "from-aurora-cyan to-aurora-blue",
     "desc": "HIPAA-compliant HIS solutions powering patient records, billing, pharmacy, and clinical workflows end-to-end.",
     "points": ["EMR / EHR", "HL7 / FHIR", "Telemedicine"]},
    {"icon": "Globe", "title": "Web Development", "gradient": "from-aurora-violet to-aurora-pink",
     "desc": "Premium web experiences built with Vue, React, and modern edge infrastructure — fast, accessible, SEO-ready.",
     "points": ["Headless CMS", "Edge rendering", "Core Web Vitals"]},
    {"icon": "Smartphone", "title": "Mobile Apps", "gradient": "from-navy-600 to-emerald-brand-500",
     "desc": "Native iOS, Android, and cross-platform Flutter apps that delight users and ship on time, every time.",
     "points": ["iOS & Android", "Flutter & React Native", "App Store strategy"]},
    {"icon": "Cloud", "title": "Cloud Solution", "gradient": "from-emerald-brand-500 to-aurora-cyan",
     "desc": "Multi-cloud architecture, migration, and FinOps on AWS, Azure, and GCP — built for resilience and cost control.",
     "points": ["Kubernetes", "Serverless", "Cost optimization"]},
    {"icon": "Webhook", "title": "API Integration", "gradient": "from-aurora-pink to-aurora-violet",
     "desc": "Connect any system to any system. We design, secure, and operate the integration fabric your business runs on.",
     "points": ["REST / GraphQL / gRPC", "Event-driven", "Legacy modernization"]},
    {"icon": "BrainCircuit", "title": "AI Solution", "gradient": "from-navy-700 to-aurora-violet",
     "desc": "Production-grade AI — RAG pipelines, fine-tuned LLMs, computer vision, and copilots that move real metrics.",
     "points": ["LLM applications", "MLOps", "Vector search"]},
]):
    db.add(m.Service(order_index=i, **sv))

reset(m.Milestone)
for i, ms in enumerate([
    {"year": "2013", "title": "Founded in San Francisco",
     "desc": "Three engineers, one shared vision: build the engineering partner they wished existed."},
    {"year": "2016", "title": "First Fortune 500 engagement",
     "desc": "Shipped a supply-chain platform that processed $1.2B in transactions in year one."},
    {"year": "2019", "title": "Expanded to 4 continents",
     "desc": "Opened studios in Singapore, London, and Jakarta — global delivery, local presence."},
    {"year": "2022", "title": "Launched SKT AI Lab",
     "desc": "Dedicated research lab shipping production AI — from copilots to vision systems."},
    {"year": "2025", "title": "320+ projects, 96% retention",
     "desc": "Trusted by category leaders to deliver the work that defines their next decade."},
]):
    db.add(m.Milestone(order_index=i, **ms))

reset(m.PortfolioItem)
for i, p in enumerate([
    {"title": "NeoBank Platform", "category": "FinTech", "size": "tall",
     "desc": "End-to-end digital banking platform serving 2.4M users with real-time ledger, KYC, and lending.",
     "image": img("1551288049-bebda4e38f71", 900), "tags": ["Vue", "Go", "Kubernetes"]},
    {"title": "MediSync HIS", "category": "Healthcare", "size": "normal",
     "desc": "Hospital Information System deployed across 14 hospitals — patient records, billing, pharmacy.",
     "image": img("1576091160550-2173dba999ef", 900), "tags": ["React", "HL7", "AWS"]},
    {"title": "ShopFlow Commerce", "category": "E-Commerce", "size": "wide",
     "desc": "Headless commerce engine processing 18M orders / yr with sub-100ms P99 latency.",
     "image": img("1556742049-0cfed4f6a45d", 900), "tags": ["Next.js", "Redis", "Edge"]},
    {"title": "Aurora AI Copilot", "category": "AI", "size": "normal",
     "desc": "Enterprise copilot with RAG over 40M documents — deployed to 14k employees in 90 days.",
     "image": img("1677442136019-21780ecad995", 900), "tags": ["LLM", "RAG", "Vector DB"]},
    {"title": "FleetIQ Logistics", "category": "Supply Chain", "size": "tall",
     "desc": "Real-time fleet and inventory platform tracking 12k vehicles across 24 countries.",
     "image": img("1586528116311-ad8dd3c8310d", 900), "tags": ["Flutter", "Kafka", "GCP"]},
    {"title": "DataPulse Analytics", "category": "Data Platform", "size": "wide",
     "desc": "Unified analytics warehouse ingesting 4TB / day from 200+ sources with sub-second queries.",
     "image": img("1551288049-1c302d55c87f", 900), "tags": ["Snowflake", "dbt", "Vue"]},
    {"title": "CloudVerse Migration", "category": "Cloud", "size": "normal",
     "desc": "Multi-cloud migration of 380 services from on-prem to AWS+GCP with zero downtime.",
     "image": img("1451187580459-43490279c0fa", 900), "tags": ["Terraform", "K8s", "FinOps"]},
    {"title": "GreenGrid Energy", "category": "IoT", "size": "normal",
     "desc": "Smart-grid analytics platform monitoring 1.2M IoT sensors across renewable energy sites.",
     "image": img("1497366216548-37526070297c", 900), "tags": ["IoT", "Time Series", "ML"]},
]):
    db.add(m.PortfolioItem(order_index=i, **p))

reset(m.ProcessStep)
for i, st in enumerate([
    {"num": "01", "title": "Discover", "icon": "Search", "desc": "We immerse in your business, users, and constraints — translating ambiguity into a sharp problem definition."},
    {"num": "02", "title": "Planning", "icon": "Map", "desc": "Roadmaps, milestones, risk register, and a delivery cadence that keeps everyone aligned from day one."},
    {"num": "03", "title": "Design", "icon": "PenTool", "desc": "Information architecture, wireframes, and a polished design system — validated with real users weekly."},
    {"num": "04", "title": "Development", "icon": "Code2", "desc": "Bi-weekly shippable increments. Trunk-based, peer-reviewed, observable from commit one."},
    {"num": "05", "title": "Testing", "icon": "ShieldCheck", "desc": "Automated, exploratory, load, security, and accessibility — quality is engineered, not bolted on."},
    {"num": "06", "title": "Deployment", "icon": "Rocket", "desc": "Blue-green or canary. Zero-drama releases with instant rollback and full audit trail."},
    {"num": "07", "title": "Support", "icon": "LifeBuoy", "desc": "24/7 SRE coverage, on-call rotations, and quarterly business reviews to keep pushing forward."},
]):
    db.add(m.ProcessStep(order_index=i, **st))

reset(m.TeamMember)
for i, t in enumerate([
    {"name": "Daniel Reyes", "role": "Founder & CEO", "img": img("1507003211169-0a1dd7228f2d", 600), "bio": "Ex-Stripe engineering leader. Builds teams that ship."},
    {"name": "Aisha Karim", "role": "CTO", "img": img("1573496359142-b8d87734a5a2", 600), "bio": "Distributed systems architect. 18 years scaling platforms."},
    {"name": "Marcus Chen", "role": "VP of Engineering", "img": img("1500648767791-00dcc994a43e", 600), "bio": "Led platform teams at Datadog and Cloudflare."},
    {"name": "Sofia Almeida", "role": "Head of Design", "img": img("1580489944761-15a19d654956", 600), "bio": "Award-winning product designer. Ex-Framer."},
    {"name": "Raj Patel", "role": "Head of AI", "img": img("1519085360753-af0119f7cbe7", 600), "bio": "PhD in ML. Ships production AI that moves metrics."},
    {"name": "Elena Volkov", "role": "VP of Delivery", "img": img("1531123897727-8f129e1688ce", 600), "bio": "Scaled Agile coach. 200+ projects delivered on time."},
    {"name": "James O'Connor", "role": "Head of Cloud", "img": img("1472099645785-5658abf4ff4e", 600), "bio": "AWS Hero. Designs multi-cloud platforms that scale."},
    {"name": "Mira Tanaka", "role": "Head of Mobile", "img": img("1494790108377-be9c29b29330", 600), "bio": "Ex-Apple iOS. Ships apps that top the charts."},
]):
    db.add(m.TeamMember(order_index=i, socials={}, **t))

reset(m.Testimonial)
for i, ts in enumerate([
    {"quote": "SKT didn't just deliver software — they re-architected how our entire engineering org thinks about quality. The platform they built now processes $4B annually with 99.99% uptime.",
     "name": "Catherine Lim", "role": "CEO, Vertex Financial", "img": img("1494790108377-be9c29b29330", 200), "rating": 5},
    {"quote": "We engaged SKT to rescue a stalled ERP migration. Six months later, we were live across 14 countries. The ROI was visible in the first quarter post-launch.",
     "name": "Roberto Sanchez", "role": "COO, Meridian Industries", "img": img("1507003211169-0a1dd7228f2d", 200), "rating": 5},
    {"quote": "The AI copilot SKT shipped for us transformed support operations. Average handle time dropped 38%. Our agents love it. Our customers love it. Our board really loves it.",
     "name": "Priya Nair", "role": "CPO, Helio Health", "img": img("1573496359142-b8d87734a5a2", 200), "rating": 5},
    {"quote": "I've worked with a dozen agencies. None come close to SKT on craft, candor, and consistency. They are simply the best engineering partner we've ever had.",
     "name": "Thomas Wright", "role": "CTO, Cascade Retail", "img": img("1519085360753-af0119f7cbe7", 200), "rating": 5},
    {"quote": "SKT rebuilt our patient records system in 9 months. It now serves 2.4M patients and has won two industry awards for usability. They are extraordinary.",
     "name": "Dr. Amara Okafor", "role": "CMIO, Lakeside Health", "img": img("1531123897727-8f129e1688ce", 200), "rating": 5},
]):
    db.add(m.Testimonial(order_index=i, **ts))

reset(m.BlogPost)
for i, bp in enumerate([
    {"title": "Why we replaced Kafka with NATS JetStream — and what we learned", "category": "Engineering",
     "excerpt": "A pragmatic comparison of Kafka and NATS JetStream for high-throughput, low-latency event-driven systems at scale.",
     "image": img("1518770660439-4636190af475", 800), "author": "Aisha Karim", "date": "May 12, 2025", "read_time": "12 min"},
    {"title": "RAG in production: 7 hard-won lessons from deploying to 14k users", "category": "AI",
     "excerpt": "Everything we wished we knew before shipping our first enterprise copilot — chunking, evals, observability, and the long tail of failure modes.",
     "image": img("1620712943543-bcc4688e7485", 800), "author": "Raj Patel", "date": "Apr 28, 2025", "read_time": "18 min"},
    {"title": "The hidden cost of premature microservices", "category": "Architecture",
     "excerpt": "A field guide to recognizing when you're about to break a monolith for the wrong reasons — and what to do instead.",
     "image": img("1555066931-4365d14bab8c", 800), "author": "Marcus Chen", "date": "Apr 14, 2025", "read_time": "9 min"},
    {"title": "Design systems that scale: from 0 to 1,200 components", "category": "Design",
     "excerpt": "How we built and governed a design system that powers 14 production apps across 3 platforms without becoming a bottleneck.",
     "image": img("1561070791-2526d30994b8", 800), "author": "Sofia Almeida", "date": "Mar 31, 2025", "read_time": "11 min"},
    {"title": "FinOps at scale: cutting a $4M cloud bill by 38%", "category": "Cloud",
     "excerpt": "The concrete tactics — from rightsizing to commitment strategy — that delivered seven-figure savings without slowing the team down.",
     "image": img("1451187580459-43490279c0fa", 800), "author": "James O'Connor", "date": "Mar 17, 2025", "read_time": "14 min"},
    {"title": "Shipping a Flutter app to 4M users: the playbook", "category": "Mobile",
     "excerpt": "Architecture, state management, CI/CD, and the release strategy that took our flagship app from idea to #1 in its category.",
     "image": img("1512941937669-90a1b58e7e9c", 800), "author": "Mira Tanaka", "date": "Mar 03, 2025", "read_time": "13 min"},
]):
    slug = bp["title"].lower().replace("'", "").replace(",", "").replace(":", "")
    slug = "-".join(slug.split())[:200]
    db.add(m.BlogPost(order_index=i, slug=slug, content="", published=True, **bp))

reset(m.Faq)
for i, f in enumerate([
    {"q": "What size engagements does SKT typically take on?",
     "a": "We work best on engagements ranging from $250k to $5M+. Smaller projects are considered when there's a clear path to a longer partnership or when the work is particularly interesting. For very small budgets, we happily refer to trusted boutique partners in our network."},
    {"q": "How quickly can you start?",
     "a": "For standard engagements, we typically mobilize a squad within 2–4 weeks of signed SOW. For urgent rescues or staff augmentation, we can have senior engineers on the ground in 5 business days. Larger teams (8+) usually take 6 weeks to assemble properly."},
    {"q": "Do you work fixed-price or time & materials?",
     "a": "Both. We default to T&M with a not-to-exceed cap for new product work where scope is still evolving, and fixed-price for well-defined migrations and integrations. We're pragmatic — the engagement model should fit the risk profile, not the other way around."},
    {"q": "Can you sign our MSA / NDA / security questionnaire?",
     "a": "Yes. We sign MSAs, NDAs, DPAs, BAAs (for healthcare), and complete vendor security questionnaires routinely. We are SOC 2 Type II certified, ISO 27001 certified, and HIPAA-compliant. Our security team can typically turn around questionnaires in 3 business days."},
    {"q": "Where are your teams located?",
     "a": "We have studios in San Francisco (HQ), Singapore, London, and Jakarta. Delivery is hybrid — a senior client-facing pod on-site or near-shore, plus a delivery pod in a region of your choice. We never offshore critical decisions; we do offshore well-scoped execution."},
    {"q": "Do you offer ongoing support after launch?",
     "a": "Yes. Most of our engagements include a 90-day warranty period, after which we transition to a managed-services SRE arrangement or train your in-house team to operate the system. 70% of our clients retain us in some capacity past launch — often for years."},
    {"q": "How do you handle IP ownership?",
     "a": "You own 100% of the IP we create for you, full stop. It's in our MSA by default. We retain rights only to pre-existing internal tools and frameworks, which are licensed to you in perpetuity. No lock-in, no surprises."},
]):
    db.add(m.Faq(order_index=i, **f))

reset(m.TrustedByLogo)
for i, name in enumerate([
    "Stripe", "Vercel", "Linear", "Framer", "Notion", "Figma", "Datadog", "Supabase",
    "Cloudflare", "HashiCorp", "GitLab", "Atlassian",
]):
    db.add(m.TrustedByLogo(order_index=i, name=name, logo_url=""))

db.commit()
db.close()
print("Seed complete: site content + all resources populated from the existing static site.")
