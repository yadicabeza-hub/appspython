from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Phase, Project

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Obtener todas las fases ordenadas
    phases = Phase.query.order_by(Phase.order).all()
    return render_template('index.html', phases=phases)

@main_bp.route('/projects')
def projects():
    # Obtener todos los proyectos con su fase actual
    all_projects = Project.query.order_by(Project.created_at.desc()).all()
    phases = Phase.query.order_by(Phase.order).all()
    return render_template('projects.html', projects=all_projects, phases=phases)

@main_bp.route('/project/add', methods=['POST'])
def add_project():
    name = request.form.get('name')
    description = request.form.get('description')
    
    # Por defecto, empieza en la fase 1 (Planificación)
    first_phase = Phase.query.order_by(Phase.order).first()
    
    if name and first_phase:
        new_project = Project(name=name, description=description, current_phase_id=first_phase.id)
        db.session.add(new_project)
        db.session.commit()
        flash('Proyecto creado exitosamente.', 'success')
    else:
        flash('Error al crear el proyecto.', 'danger')
        
    return redirect(url_for('main.projects'))

@main_bp.route('/project/update/<int:project_id>', methods=['POST'])
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    new_phase_id = request.form.get('phase_id')
    
    if new_phase_id:
        project.current_phase_id = new_phase_id
        db.session.commit()
        flash('Fase del proyecto actualizada.', 'success')
        
    return redirect(url_for('main.projects'))

@main_bp.route('/project/delete/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('Proyecto eliminado.', 'info')
    return redirect(url_for('main.projects'))
