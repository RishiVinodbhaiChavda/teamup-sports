"""
Location Routes - Country/State/City dropdown data
Uses CountriesNow API for location data
"""
import requests
from flask import Blueprint, request, jsonify

locations_bp = Blueprint('locations', __name__)

# Cache location data to avoid repeated API calls
_cache = {}


@locations_bp.route('/countries', methods=['GET'])
def get_countries():
    """Get list of all countries"""
    if 'countries' in _cache:
        return jsonify({'countries': _cache['countries']})
    
    try:
        resp = requests.get('https://countriesnow.space/api/v0.1/countries', timeout=10)
        data = resp.json()
        
        if data.get('error'):
            return jsonify({'countries': ['India']}), 200
        
        countries = sorted(set(item['country'] for item in data.get('data', [])))
        _cache['countries'] = countries
        return jsonify({'countries': countries})
    except Exception:
        return jsonify({'countries': ['India']})


@locations_bp.route('/states', methods=['GET'])
def get_states():
    """Get states for a country"""
    country = request.args.get('country', 'India')
    cache_key = f'states_{country}'
    
    if cache_key in _cache:
        return jsonify({'states': _cache[cache_key]})
    
    try:
        resp = requests.post(
            'https://countriesnow.space/api/v0.1/countries/states',
            json={'country': country},
            timeout=10
        )
        data = resp.json()
        
        if data.get('error'):
            return jsonify({'states': []}), 200
        
        states = sorted([s['name'] for s in data.get('data', {}).get('states', [])])
        _cache[cache_key] = states
        return jsonify({'states': states})
    except Exception:
        return jsonify({'states': []})


@locations_bp.route('/cities', methods=['GET'])
def get_cities():
    """Get cities for a state in a country"""
    country = request.args.get('country', 'India')
    state = request.args.get('state', '')
    cache_key = f'cities_{country}_{state}'
    
    if cache_key in _cache:
        return jsonify({'cities': _cache[cache_key]})
    
    try:
        resp = requests.post(
            'https://countriesnow.space/api/v0.1/countries/state/cities',
            json={'country': country, 'state': state},
            timeout=10
        )
        data = resp.json()
        
        if data.get('error'):
            return jsonify({'cities': []}), 200
        
        cities = sorted(data.get('data', []))
        _cache[cache_key] = cities
        return jsonify({'cities': cities})
    except Exception:
        return jsonify({'cities': []})
