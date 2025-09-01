#!/usr/bin/env python3
"""
Swedish Restaurant Heat Menu Checker
Detects if both 'pannkakor' and 'stuvade makaroner' are served on the same day.
"""

import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import argparse


def check_menu_for_target_dishes(verbose=False):
    """
    Main function to check if both target dishes appear on the same day.
    Returns True if both dishes are found on the same day, False otherwise.
    """
    # Target dishes to find
    target_dishes = ['pannkakor', 'stuvade makaroner']
    
    # Swedish weekdays
    weekdays = ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag']
    
    try:
        if verbose:
            print("=== HEAT RESTAURANG MENY KONTROLL ===")
            print(f"Söker efter: {target_dishes}")
            print(f"På veckodagar: {weekdays}")
            print("\nHämtar menydata från XML-källa...")
        
        # Fetch and parse the XML data directly
        daily_menus = parse_daily_menus(verbose)
        
        # Check each day for both dishes
        for day, menu_items in daily_menus.items():
            has_pannkakor = any('pannkakor' in item.lower() for item in menu_items)
            has_stuvade_makaroner = any('stuvade makaroner' in item.lower() for item in menu_items)
            
            if verbose:
                print(f"\n{day.title()}:")
                print(f"  Rätter hittade:")
                for item in menu_items:
                    print(f"    - {item}")
                print(f"  Har pannkakor: {has_pannkakor}")
                print(f"  Har stuvade makaroner: {has_stuvade_makaroner}")
            
            if has_pannkakor and has_stuvade_makaroner:
                if verbose:
                    print(f"  ✓ BÅDA RÄTTERNA HITTADE PÅ {day.upper()}!")
                return True
        
        if verbose:
            print("\n❌ Båda rätterna hittades inte samma dag")
        return False
        
    except Exception as e:
        if verbose:
            print(f"Fel: {e}")
        return False


def parse_daily_menus(verbose=False):
    """
    Parse the XML endpoint to extract menu items for each weekday.
    Returns dict with weekday -> list of menu items.
    """
    try:
        # The XML endpoint discovered from the JavaScript
        xml_url = "https://castit.nu/xml/posts.php?c=72&h=a800e34fa2c8f36034180c3f29eedd73&ct=58&s=945"
        
        # Fetch the XML data
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(xml_url, headers=headers)
        response.raise_for_status()
        
        # Parse XML
        root = ET.fromstring(response.content)
        
        daily_menus = {
            'måndag': [],
            'tisdag': [],
            'onsdag': [],
            'torsdag': [],
            'fredag': []
        }
        
        # Find the menu item in the XML
        item = root.find('.//item')
        if item is None:
            if verbose:
                print("Ingen meny hittades i XML")
            return daily_menus
            
        # Extract Monday dishes (mandagratt1-6)
        for i in range(1, 7):
            rubrik = item.find(f'mandagratt{i}rubrik')
            if rubrik is not None and rubrik.text and rubrik.text.strip():
                daily_menus['måndag'].append(rubrik.text.strip())
        
        # Extract Tuesday dishes (tisdagratt1-6)
        for i in range(1, 7):
            rubrik = item.find(f'tisdagratt{i}rubrik')
            if rubrik is not None and rubrik.text and rubrik.text.strip():
                daily_menus['tisdag'].append(rubrik.text.strip())
        
        # Extract Wednesday dishes (onsdagratt1-6)
        for i in range(1, 7):
            rubrik = item.find(f'onsdagratt{i}rubrik')
            if rubrik is not None and rubrik.text and rubrik.text.strip():
                daily_menus['onsdag'].append(rubrik.text.strip())
        
        # Extract Thursday dishes (torsdagratt1-8)
        for i in range(1, 9):
            rubrik = item.find(f'torsdagratt{i}rubrik')
            if rubrik is not None and rubrik.text and rubrik.text.strip():
                daily_menus['torsdag'].append(rubrik.text.strip())
        
        # Extract Friday dishes (fredagratt1-8)
        for i in range(1, 9):
            rubrik = item.find(f'fredagratt{i}rubrik')
            if rubrik is not None and rubrik.text and rubrik.text.strip():
                daily_menus['fredag'].append(rubrik.text.strip())
        
        return daily_menus
        
    except requests.RequestException as e:
        if verbose:
            print(f"Fel vid hämtning av XML-data: {e}")
        return {day: [] for day in ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag']}
    except ET.ParseError as e:
        if verbose:
            print(f"Fel vid tolkning av XML: {e}")
        return {day: [] for day in ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag']}
    except Exception as e:
        if verbose:
            print(f"Fel vid behandling av menydata: {e}")
        return {day: [] for day in ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag']}


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Min Stora Dag - Väntar på den perfekta lunchen när pannkakor och stuvade makaroner serveras samma dag på Heat')
    parser.add_argument('--verbose', '-v', action='store_true', help='Visa detaljerad information om meny parsing')
    
    args = parser.parse_args()
    
    result = check_menu_for_target_dishes(verbose=args.verbose)
    
    if args.verbose:
        print(f"\nResultat: {'Båda rätterna hittades samma dag!' if result else 'Rätterna inte samma dag'}")
    else:
        print(result)
    
    return result


if __name__ == "__main__":
    main()