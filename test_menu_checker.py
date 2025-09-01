#!/usr/bin/env python3
"""
Simple tests for the menu checker functionality.
"""

def test_dish_detection():
    """Test the dish detection logic with various text patterns."""
    
    test_cases = [
        # (menu_text, should_find_pannkakor, should_find_stuvade_makaroner)
        ("Idag serverar vi pannkakor med sylt", True, False),
        ("Stuvade makaroner med korv", False, True),
        ("Pannkakor och stuvade makaroner", True, True),
        ("PANNKAKOR med grädde", True, False),  # Case insensitive
        ("Stuvade MAKARONER serveras", False, True),  # Case insensitive
        ("Pasta och kött", False, False),
        ("Vi har pannkakor idag samt stuvade makaroner", True, True),
        ("Pannkakor. Stuvade makaroner.", True, True),
    ]
    
    print("=== TESTING DISH DETECTION LOGIC ===")
    
    for i, (text, expected_pannkakor, expected_stuvade_makaroner) in enumerate(test_cases, 1):
        has_pannkakor = 'pannkakor' in text.lower()
        has_stuvade_makaroner = 'stuvade makaroner' in text.lower()
        
        success = (has_pannkakor == expected_pannkakor and 
                  has_stuvade_makaroner == expected_stuvade_makaroner)
        
        status = "✓ PASS" if success else "❌ FAIL"
        print(f"Test {i}: {status}")
        print(f"  Text: '{text}'")
        print(f"  Expected: pannkakor={expected_pannkakor}, stuvade_makaroner={expected_stuvade_makaroner}")
        print(f"  Actual:   pannkakor={has_pannkakor}, stuvade_makaroner={has_stuvade_makaroner}")
        print()

def test_day_parsing():
    """Test parsing of Swedish weekdays."""
    
    weekdays = ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag']
    
    sample_html_patterns = [
        "<h2>Måndag</h2><p>Pannkakor med sylt</p>",
        "<div class='day'>Tisdag</div><ul><li>Stuvade makaroner</li></ul>",
        "ONSDAG: Pannkakor och stuvade makaroner",
        "Torsdag - Kött med potatis",
        "På fredag serverar vi fisk"
    ]
    
    print("=== TESTING DAY PARSING PATTERNS ===")
    
    for i, html in enumerate(sample_html_patterns, 1):
        print(f"Pattern {i}: {html}")
        
        # Simple day detection (in real implementation, we'd use BeautifulSoup)
        found_days = []
        for day in weekdays:
            if day.lower() in html.lower():
                found_days.append(day)
        
        print(f"  Found days: {found_days}")
        print()

if __name__ == "__main__":
    test_dish_detection()
    test_day_parsing()