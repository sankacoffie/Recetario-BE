from flask import Blueprint, request, jsonify
from app.models import db, Recipe, Menu
from app.scraping import scrape_recipe
from app.utils import consolidate_ingredients

main = Blueprint('main', __name__)

@main.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.json
    recipe = Recipe(title=data['title'], ingredients=data['ingredients'], steps=data['steps'])
    db.session.add(recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe added successfully'}), 201

@main.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    recipe_data = scrape_recipe(data['url'])
    return jsonify(recipe_data), 200

@main.route('/menu', methods=['POST'])
def create_menu():
    data = request.json
    menu = Menu(user_id=data['user_id'], recipes=data['recipes'], date=data['date'])
    db.session.add(menu)
    db.session.commit()
    return jsonify({'message': 'Menu created successfully'}), 201

@main.route('/shopping-list', methods=['POST'])
def shopping_list():
    data = request.json
    recipes = Recipe.query.filter(Recipe.id.in_(data['recipe_ids'])).all()
    consolidated = consolidate_ingredients(recipes)
    return jsonify(consolidated), 200
