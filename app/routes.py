from flask import Blueprint, jsonify
from .models import TeamMember, About, Service, FAQ, Contact, Home, Article

main_bp = Blueprint('main', __name__)

@main_bp.route('/team', methods=['GET'])
def get_team():
    team_members = TeamMember.query.all()
    return jsonify([t.to_dict() for t in team_members])

@main_bp.route('/about', methods=['GET'])
def get_about():
    about_info = About.query.all()
    return jsonify([a.to_dict() for a in about_info])

@main_bp.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([s.to_dict() for s in services])

@main_bp.route('/faqs', methods=['GET'])
def get_faqs():
    faqs = FAQ.query.all()
    return jsonify([f.to_dict() for f in faqs])

@main_bp.route('/contact', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([c.to_dict() for c in contacts])

@main_bp.route('/home', methods=['GET'])
def get_home():
    home_content = Home.query.all()
    return jsonify([h.to_dict() for h in home_content])

@main_bp.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    return jsonify([a.to_dict() for a in articles])
