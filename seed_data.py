import sys
sys.path.append('app')
from app import create_app, db
from app.models import TeamMember, Article, Home, About, Service, Contact, FAQ
from datetime import datetime

app = create_app()

with app.app_context():
    # Seed Team Members with images
    team_member_1 = TeamMember(
        name="Kennedy Auka", 
        role="Managing Partner", 
        bio="John is aan expert in corporate law and mergers & acquisitions.",
        image_url="https://res.cloudinary.com/demo/image/upload/v1584562210/sample_john.jpg"  # Example Cloudinary image URL
    )
    team_member_2 = TeamMember(
        name="Jane Smith", 
        role="Senior Associate", 
        bio="Jane specializes in family law and estate planning.",
        image_url="https://res.cloudinary.com/demo/image/upload/v1584562210/sample_jane.jpg"  # Example Cloudinary image URL
    )

    # Seed Articles
    article_1 = Article(
        title="Legal Insights on Corporate Law",
        content="This article explores the latest trends in corporate law...",
        image_url="https://res.cloudinary.com/dtpe9altr/image/upload/v1735433437/Corporate_bkdusz.jpg",
        created_at=datetime.now()
    )
    article_2 = Article(
        title="The Importance of Estate Planning",
        content="Estate planning is an essential tool for ensuring your assets are distributed according to your wishes...",
        image_url="https://res.cloudinary.com/dtpe9altr/image/upload/v1735433437/estate_planning_nwqp1n.jpg",
        created_at=datetime.now()
    )

    # Seed Home Page Content
    home = Home(
        title="Welcome to Our Law Firm",
        subtitle="Your Trusted Legal Partner",
        image_url="https://res.cloudinary.com/dtpe9altr/image/upload/v1735432710/Home_v7f89x.jpg",
        content="We offer a wide range of legal services including corporate law, estate planning, and more..."
    )

    # Seed About Page Content
    about = About(
        title="About Us",
        content="Our law firm has been providing legal services for over 30 years. We specialize in corporate law, family law, and estate planning."
    )

    # Seed Services
    service_1 = Service(name="Corporate Law", description="We offer expert legal advice for corporations, including mergers, acquisitions, and compliance.")
    service_2 = Service(name="Estate Planning", description="Our team helps you plan for the future by providing comprehensive estate planning services.")
    service_3 = Service(name="Family Law", description="We handle all aspects of family law including divorce, custody, and prenuptial agreements.")

    # Seed Contact Information
    contact = Contact(
        address="40, 00509, Mbagathi",
        phone="+254 712 456 789",
        email="info@lawfirm.com",
        social_links={"facebook": "http://facebook.com/lawfirm", "twitter": "http://twitter.com/lawfirm"}
    )

    # Seed FAQ
    faq_1 = FAQ(question="What should I do if I need legal advice?", answer="Contact us to schedule a consultation with one of our expert attorneys.")
    faq_2 = FAQ(question="How much do your services cost?", answer="Our pricing is based on the type of services required. Please contact us for a quote.")

    # Add all the records to the session
    db.session.add(team_member_1)
    db.session.add(team_member_2)
    db.session.add(article_1)
    db.session.add(article_2)
    db.session.add(home)
    db.session.add(about)
    db.session.add(service_1)
    db.session.add(service_2)
    db.session.add(service_3)
    db.session.add(contact)
    db.session.add(faq_1)
    db.session.add(faq_2)

    # Commit to the database
    db.session.commit()
    print("Sample data added to the database!")
