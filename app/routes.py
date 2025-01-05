from flask import Blueprint, jsonify
from .models import TeamMember, About, Service, FAQ, Contact, Home, Article
from .app import db

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

@main_bp.route('/delete_service_by_id/<int:service_id>', methods=['POST'])
def delete_service_by_id(service_id):
    try:
        # Query the Service model to find the service by ID
        service = Service.query.get(service_id)

        # If the service exists, delete it
        if service:
            db.session.delete(service)
            db.session.commit()
            return jsonify({"message": f"Service with ID {service_id} deleted successfully."}), 200
        else:
            # Return an error if the service is not found
            return jsonify({"error": "Service not found."}), 404
    except Exception as e:
        # Rollback the session and return an error message if something goes wrong
        db.session.rollback()
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@main_bp.route('/delete_team_member_by_id/<int:member_id>', methods=['POST'])
def delete_team_member_by_id(member_id):
    try:
        # Query the TeamMember model for the specified ID
        member = TeamMember.query.get(member_id)
        if not member:
            return jsonify({"error": "Team member not found"}), 404

        # Delete the member and commit the changes
        db.session.delete(member)
        db.session.commit()
        return jsonify({"message": f"Team member with ID {member_id} deleted successfully."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

