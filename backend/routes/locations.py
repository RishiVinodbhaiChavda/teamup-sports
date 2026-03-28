"""
Location Routes - Country/State/City dropdown data
Uses CountriesNow API for location data
"""
import requests
from flask import Blueprint, request, jsonify

locations_bp = Blueprint('locations', __name__)

# Cache location data to avoid repeated API calls
_cache = {}


# Comprehensive Fallbacks for when the API is down/slow
FALLBACK_DATA = {
    'countries': sorted([
        "India", "United States", "United Kingdom", "Canada", "Australia", 
        "United Arab Emirates", "Saudi Arabia", "Singapore", "Germany", 
        "France", "Japan", "Italy", "Spain", "Russia", "Brazil", "South Africa",
        "Netherlands", "Switzerland", "New Zealand", "Sweden", "Israel"
    ]),
    'states_India': sorted([
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", 
        "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", 
        "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", 
        "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
        "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
        "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
    ]),
    'cities_India_Delhi': ["New Delhi", "North Delhi", "South Delhi", "West Delhi", "East Delhi"],
    'cities_India_Gujarat': ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Gandhinagar"],
    'cities_India_Maharashtra': ["Mumbai", "Pune", "Nagpur", "Thane", "Nashik", "Aurangabad", "Solapur"],
    'cities_India_Karnataka': ["Bangalore", "Hubli", "Mysore", "Gulbarga", "Belgaum", "Mangalore"],
    'cities_India_Tamil Nadu': ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli"],
    'cities_India_Uttar Pradesh': ["Lucknow", "Kanpur", "Ghaziabad", "Agra", "Meerut", "Varanasi", "Prayagraj"],
    'cities_India_West Bengal': ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri"],
    'cities_India_Rajasthan': ["Jaipur", "Jodhpur", "Kota", "Bikaner", "Ajmer", "Udaipur"],
    'cities_India_Punjab': ["Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda"],
    'cities_India_Haryana': ["Faridabad", "Gurgaon", "Panipat", "Ambala", "Yamunanagar"]
}


@locations_bp.route('/countries', methods=['GET'])
def get_countries():
    """Get list of all countries"""
    if 'countries' in _cache:
        return jsonify({'countries': _cache['countries']})
    
    try:
        resp = requests.get('https://countriesnow.space/api/v0.1/countries', timeout=10)
        data = resp.json()
        
        if data.get('error'):
            raise Exception("API Error")
        
        countries = sorted(set(item['country'] for item in data.get('data', [])))
        if not countries:
            raise Exception("Empty country list")
            
        _cache['countries'] = countries
        return jsonify({'countries': countries})
    except Exception as e:
        print(f"[LOCATIONS] Countries API Failed: {str(e)}. Using static fallback.")
        # Fallback to a diverse list of countries
        return jsonify({'countries': FALLBACK_DATA['countries']})


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
            raise Exception("API Error")
        
        states = sorted([s['name'] for s in data.get('data', {}).get('states', [])])
        if not states:
            raise Exception("Empty state list")
            
        _cache[cache_key] = states
        return jsonify({'states': states})
    except Exception as e:
        print(f"[LOCATIONS] States API Failed for {country}: {str(e)}. Using static fallback.")
        # Fallback for India or return empty
        fallback_key = f'states_{country}'
        return jsonify({'states': FALLBACK_DATA.get(fallback_key, [])})


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
            raise Exception("API Error")
        
        cities = sorted(data.get('data', []))
        if not cities:
            raise Exception("Empty city list")
            
        _cache[cache_key] = cities
        return jsonify({'cities': cities})
    except Exception as e:
        print(f"[LOCATIONS] Cities API Failed for {state}, {country}: {str(e)}. Using static fallback.")
        # Fallback for specific Indian states
        fallback_key = f'cities_{country}_{state}'
        return jsonify({'cities': FALLBACK_DATA.get(fallback_key, [])})
